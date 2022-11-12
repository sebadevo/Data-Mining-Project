import mysql.connector
import pandas as pd
def get_connection():
    return mysql.connector.connect(host='localhost', database='stib', user='stib', password='Stib1234!')

def close_connection(connection):
    if connection:
        connection.close()

def read_database_version():
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT version();")
        db_version = cursor.fetchone()
        print("You are connected to MySQL version: ", db_version)
        close_connection(connection)
    except (Exception, mysql.connector.Error) as error:
        print("Error while getting data", error)

def test_dataframe():
    connection = get_connection()
    query = "Select * from stops;"
    result_dataFrame = pd.read_sql(query,con= connection)
    print(result_dataFrame)
    close_connection(connection)


test_dataframe()

