import psycopg2
from psycopg2.extras import RealDictCursor

def sql_select(query):
    db_connection = psycopg2.connect("dbname=pet_adoption")
    db_cursor = db_connection.cursor(cursor_factory=RealDictCursor)

    db_cursor.execute(query)    
    results = db_cursor.fetchall()

    db_cursor.close()
    db_connection.close()
    return results

def sql_select_one(query, params):
    db_connection = psycopg2.connect("dbname=pet_adoption")
    db_cursor = db_connection.cursor()

    db_cursor.execute(query, params)    
    result = db_cursor.fetchone()

    return result

def sql_write(query, params):
    db_connection = psycopg2.connect("dbname=pet_adoption")
    db_cursor = db_connection.cursor()
        
    db_cursor.execute(
        query,
        params
    )
    
    db_connection.commit()
    db_cursor.close()
    db_connection.close()