import pandas as pd
import numpy as np
from sklearn import cluster
from utils import time_to_sec


def load_data_and_merge(route,trips,stop_times,calendar):
    routes_data = pd.read_csv(route, sep=",")
    trips_data = pd.read_csv(trips, sep=",")
    stop_times_data = pd.read_csv(stop_times, sep=",")
    calendar_data = pd.read_csv(calendar, sep=",")
    trips_routes_merge = pd.merge(trips_data, routes_data, on='route_id')
    trips_routes_merge = trips_routes_merge.loc[trips_routes_merge['route_type'] == 0]
    trips_routes_calendar = pd.merge(trips_routes_merge, calendar_data, on='service_id')
    trips_routes_calender_stops = pd.merge(stop_times_data, trips_routes_calendar, on='trip_id')
    trips_routes_calender_stops.drop(['route_desc','route_type','route_color','route_text_color', 'shape_id','route_url','end_date', 'tuesday', 'wednesday', 'thursday', 'friday', 'block_id','pickup_type', 'drop_off_type', 'stop_sequence', 'departure_time', 'trip_id'], inplace=True, axis=1)
    return trips_routes_calender_stops

def filter(data, direction_id, saterday, stop_id, short_name, start_date):
    data = data.loc[(data['direction_id'] == direction_id) & (data['saturday'] == saterday) & (data['stop_id'] == stop_id) & (data['route_short_name'] == short_name)& (data['start_date'] == start_date)]
    return data


def compute_time_difference(data):
    arrival_times = data['arrival_time'].tolist()
    arrival_times_minutes = map(time_to_sec, arrival_times)
    arrival_times_minutes = sorted(arrival_times_minutes)
    print(arrival_times_minutes)
    print(len(arrival_times_minutes))
    x, y = [], []
    for i in range(len(arrival_times_minutes)-1):
        y.append(round((arrival_times_minutes[i+1]-arrival_times_minutes[i])/60, 2))
        x.append(round(arrival_times_minutes[i]/3600, 2))
    return x,y

def retrieve_info_title(data,stop_id):
    stop = pd.read_csv("data/gtfs3Sept/stops.csv", sep=",")

    name_stop = stop.loc[stop['stop_id'] == stop_id]

    name_stop = name_stop["stop_name"].item()
    print(name_stop)
    trip_headsign = data['trip_headsign'].iat[0]
    route_name = data['route_long_name'].iat[0]
    return trip_headsign,route_name, name_stop