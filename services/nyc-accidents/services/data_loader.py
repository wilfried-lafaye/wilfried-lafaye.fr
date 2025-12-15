import pandas as pd
import requests
from config.database import API_URL
from models.database import get_connection

def load_data_from_api(limit=10000):
    """Charge les données depuis l'API NYC"""
    try:
        response = requests.get(API_URL, params={'$limit': limit})
        response.raise_for_status()
        data = response.json()
        df = pd.DataFrame(data)
        
        # Formatage des dates
        if 'crash_date' in df.columns:
            df['crash_date'] = pd.to_datetime(df['crash_date'])
            df['crash_date'] = df['crash_date'].dt.strftime('%Y-%m-%d')
        
        return df
    except Exception as e:
        raise Exception(f"Erreur lors du chargement des données: {e}")

def get_missing_data_stats(df):
    """Retourne les statistiques des données manquantes"""
    missing_percent = df.isna().mean() * 100
    missing_percent = missing_percent[missing_percent > 0].sort_values(ascending=False)
    
    total_missing = df.isna().sum().sum()
    total_cells = df.size
    
    return missing_percent, total_missing, total_cells

def insert_data_to_db(df):
    """Insère les données dans la base SQLite"""
    conn = get_connection()
    cur = conn.cursor()
    
    # 1) Table Lieu
    lieu_cols = [
        "zip_code", "borough", "on_street_name", 
        "cross_street_name", "off_street_name", "latitude", "longitude"
    ]
    
    for col in lieu_cols:
        if col not in df.columns:
            df[col] = None
    
    lieu_df = df[lieu_cols + ["collision_id"]].copy()
    lieu_df["id_location"] = lieu_df.index
    
    cur.executemany(
        """
        INSERT OR IGNORE INTO Lieu (
            id_location, zip_code, borough, on_street_name, 
            cross_street_name, off_street_name, latitude, longitude
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """,
        [
            (
                int(row["id_location"]),
                row["zip_code"],
                row["borough"],
                row["on_street_name"],
                row["cross_street_name"],
                row["off_street_name"],
                float(row["latitude"]) if row["latitude"] is not None else None,
                float(row["longitude"]) if row["longitude"] is not None else None,
            )
            for _, row in lieu_df.iterrows()
        ]
    )
    
    # 2) Table Accident
    accident_df = df.copy()
    accident_df["id_location"] = accident_df.index
    
    accident_cols = [
        "collision_id", "crash_date", "crash_time", "id_location",
        "number_of_persons_injured", "number_of_persons_killed",
        "number_of_pedestrians_injured", "number_of_pedestrians_killed",
        "number_of_cyclist_injured", "number_of_cyclist_killed",
        "number_of_motorist_injured", "number_of_motorist_killed",
    ]
    
    for col in accident_cols:
        if col not in accident_df.columns:
            accident_df[col] = None
    
    cur.executemany(
        f"""
        INSERT OR IGNORE INTO Accident (
            {", ".join(accident_cols)}
        ) VALUES ({", ".join(["?"] * len(accident_cols))})
        """,
        [
            tuple(
                int(row[col]) if col in ["collision_id", "id_location"] and pd.notna(row[col]) else row[col] 
                for col in accident_cols
            )
            for _, row in accident_df.iterrows()
        ]
    )
    
    # 3) Remplir les tables de véhicules et facteurs
    fill_vehicle_tables(df, cur)
    
    conn.commit()
    conn.close()

def fill_vehicle_tables(df, cursor):
    """Remplit les tables VehiculeType, VehiculeInAccident et FacteurContributif"""
    
    # Dictionnaire pour mapper les types de véhicules à des IDs
    vehicle_type_mapping = {}
    vehicle_type_id = 1
    
    # Parcourir toutes les colonnes de véhicules (vehicle_type_code1 à vehicle_type_code5)
    for vehicle_num in range(1, 6):
        vehicle_type_col = f'vehicle_type_code{vehicle_num}'
        factor_col = f'contributing_factor_vehicle{vehicle_num}'
        
        if vehicle_type_col in df.columns:
            for _, row in df.iterrows():
                collision_id = row.get('collision_id')
                vehicle_type = row.get(vehicle_type_col)
                factor = row.get(factor_col) if factor_col in df.columns else None
                
                # Vérifier que l'accident et le type de véhicule existent
                if (collision_id is not None and pd.notna(collision_id) and 
                    vehicle_type is not None and pd.notna(vehicle_type) and 
                    vehicle_type != ''):

                    # Ajouter le type de véhicule au mapping s'il n'existe pas
                    if vehicle_type not in vehicle_type_mapping:
                        vehicle_type_mapping[vehicle_type] = vehicle_type_id
                        
                        # Insérer dans VehiculeType
                        cursor.execute(
                            "INSERT OR IGNORE INTO VehiculeType (id_type, type) VALUES (?, ?)",
                            (vehicle_type_id, vehicle_type)
                        )
                        vehicle_type_id += 1
                    
                    # Insérer dans VehiculeInAccident
                    cursor.execute(
                        """
                        INSERT OR IGNORE INTO VehiculeInAccident 
                        (collision_id, vehicle_number, id_type) 
                        VALUES (?, ?, ?)
                        """,
                        (int(collision_id), vehicle_num, vehicle_type_mapping[vehicle_type])
                    )
                    
                    # Insérer dans FacteurContributif si le facteur existe
                    if (factor is not None and pd.notna(factor) and 
                        factor != '' and factor != 'Unspecified'):
                        cursor.execute(
                            """
                            INSERT OR IGNORE INTO FacteurContributif 
                            (collision_id, vehicle_number, factor) 
                            VALUES (?, ?, ?)
                            """,
                            (int(collision_id), vehicle_num, factor)
                        )
