import sqlite3
from config.database import DB_PATH

def get_connection():
    """Retourne une connexion à la base de données"""
    return sqlite3.connect(DB_PATH)

def create_tables():
    """Crée les tables de la base de données"""
    conn = get_connection()
    cur = conn.cursor()

    sql_statements = [
        """
        CREATE TABLE IF NOT EXISTS Lieu (
            id_location INTEGER PRIMARY KEY,
            zip_code TEXT,
            borough TEXT,
            on_street_name TEXT,
            cross_street_name TEXT,
            off_street_name TEXT,
            latitude REAL,
            longitude REAL
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS Accident (
            collision_id INTEGER PRIMARY KEY,
            crash_date TEXT NOT NULL,
            crash_time TEXT NOT NULL,
            id_location INTEGER NOT NULL,
            number_of_persons_injured INTEGER,
            number_of_persons_killed INTEGER,
            number_of_pedestrians_injured INTEGER,
            number_of_pedestrians_killed INTEGER,
            number_of_cyclist_injured INTEGER,
            number_of_cyclist_killed INTEGER,
            number_of_motorist_injured INTEGER,
            number_of_motorist_killed INTEGER,
            FOREIGN KEY(id_location) REFERENCES Lieu(id_location)
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS VehiculeType (
            id_type INTEGER PRIMARY KEY,
            type TEXT
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS VehiculeInAccident (
            collision_id INTEGER NOT NULL,
            vehicle_number INTEGER NOT NULL,
            id_type INTEGER,
            PRIMARY KEY(collision_id, vehicle_number),
            FOREIGN KEY(collision_id) REFERENCES Accident(collision_id),
            FOREIGN KEY(id_type) REFERENCES VehiculeType(id_type)
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS FacteurContributif (
            collision_id INTEGER NOT NULL,
            vehicle_number INTEGER NOT NULL,
            factor TEXT,
            PRIMARY KEY(collision_id, vehicle_number),
            FOREIGN KEY(collision_id, vehicle_number)
                REFERENCES VehiculeInAccident(collision_id, vehicle_number)
        );
        """
    ]

    for statement in sql_statements:
        cur.execute(statement)
    
    conn.commit()
    conn.close()
