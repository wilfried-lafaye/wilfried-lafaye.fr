import pandas as pd
from models.database import get_connection

def execute_query(query, params=None):
    """Executes a SQL query and returns results"""
    conn = get_connection()
    try:
        if query.strip().upper().startswith('SELECT'):
            df = pd.read_sql_query(query, conn, params=params)
            return df, None
        else:
            cur = conn.cursor()
            cur.execute(query, params or ())
            conn.commit()
            return None, f"{cur.rowcount} row(s) affected"
    except Exception as e:
        return None, f"Error: {e}"
    finally:
        conn.close()

def get_table_info():
    """Returns information about tables"""
    query = "SELECT name FROM sqlite_master WHERE type='table'"
    result, error = execute_query(query)
    return result, error

def get_sample_data(table_name, limit=5):
    """Returns a sample of data from a table"""
    query = f"SELECT * FROM {table_name} LIMIT {limit}"
    return execute_query(query)

def get_accidents_by_borough():
    """Returns the number of accidents by borough"""
    query = """
    SELECT borough, COUNT(*) as nb_accidents 
    FROM Lieu 
    WHERE borough IS NOT NULL 
    GROUP BY borough 
    ORDER BY nb_accidents DESC
    """
    return execute_query(query)

def get_daily_accidents_stats():
    """Returns accident statistics by day (last 30 days)"""
    query = """
    SELECT * FROM (
        SELECT crash_date, COUNT(*) as accidents_par_jour 
        FROM Accident 
        GROUP BY crash_date 
        ORDER BY crash_date DESC 
        LIMIT 30
    ) ORDER BY crash_date ASC
    """
    return execute_query(query)

def get_accidents_by_hour():
    """Returns the number of accidents by hour of day"""
    query = """
    SELECT 
        CAST(substr(crash_time, 1, instr(crash_time, ':') - 1) AS INTEGER) as hour,
        COUNT(*) as nb_accidents
    FROM Accident
    WHERE crash_time IS NOT NULL
    GROUP BY hour
    ORDER BY hour ASC
    """
    return execute_query(query)

def get_fatal_accidents():
    """Returns accidents with fatalities"""
    query = """
    SELECT collision_id, crash_date, crash_time, 
           number_of_persons_injured, number_of_persons_killed 
    FROM Accident 
    WHERE number_of_persons_killed > 0 
    ORDER BY crash_date DESC 
    LIMIT 20
    """
    return execute_query(query)
