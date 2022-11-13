import mysql.connector
import pandas as pd
from dashboard.enumeration import Day 

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

def load_dataframe(day,type,direction_id, stop_id, short_name, start_date):
    if day == Day.Saterday:
        query = ("select st.arrival_time, st.stop_id, tr.route_id, tr.service_id, tr.trip_headsign, tr.direction_id, ro.routes_short_name, ro.routes_long_name, ca.saturday, ca.sunday, ca.monday, ca.start_date"
        " from trips tr" 
        " inner join routes ro on tr.route_id = ro.routes_id"
        " inner join stop_times st on st.trip_id = tr.trip_id"
        " inner join calendar ca on ca.service_id = tr.service_id"
        " where ro.route_type = %s and ca.saturday = 1 and tr.direction_id = %s"
        " and st.stop_id = %s and ro.routes_short_name = %s and ca.start_date = %s;")
    elif day == Day.Sunday:
        query = ("select st.arrival_time, st.stop_id, tr.route_id, tr.service_id, tr.trip_headsign, tr.direction_id, ro.routes_short_name, ro.routes_long_name, ca.saturday, ca.sunday, ca.monday, ca.start_date"
        " from trips tr" 
        " inner join routes ro on tr.route_id = ro.routes_id"
        " inner join stop_times st on st.trip_id = tr.trip_id"
        " inner join calendar ca on ca.service_id = tr.service_id"
        " where ro.route_type = %s and ca.sunday = 1 and tr.direction_id = %s"
        " and st.stop_id = %s and ro.routes_short_name = %s and ca.start_date = %s;")
    else:
        query = ("select st.arrival_time, st.stop_id, tr.route_id, tr.service_id, tr.trip_headsign, tr.direction_id, ro.routes_short_name, ro.routes_long_name, ca.saturday, ca.sunday, ca.monday, ca.start_date"
        " from trips tr" 
        " inner join routes ro on tr.route_id = ro.routes_id"
        " inner join stop_times st on st.trip_id = tr.trip_id"
        " inner join calendar ca on ca.service_id = tr.service_id"
        " where ro.route_type = %s and ca.monday = 1 and tr.direction_id = %s"
        " and st.stop_id = %s and ro.routes_short_name = %s and ca.start_date = %s;")

    connection = get_connection()
    data = pd.read_sql(query,params=[type,direction_id, stop_id, short_name, start_date],con= connection)
    close_connection(connection)
    return data;