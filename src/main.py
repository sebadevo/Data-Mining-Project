import pandas as pd
import numpy
import json


file_mode = "../data/ACTU_STOPS_0.csv"
file_trips = "../data/gtfs3Sept/trips.csv"
file_routes = "../data/gtfs3Sept/routes.csv"
file_stop_times = "../data/gtfs3Sept/stop_times.csv"
file_stops = "../data/gtfs3Sept/stops.csv"
file_calendar = "../data/gtfs3Sept/calendar.csv"


df_mode = pd.read_csv(file_mode)
df_trips = pd.read_csv(file_trips)
df_routes = pd.read_csv(file_routes)
df_stop_times = pd.read_csv(file_stop_times)
df_stops = pd.read_csv(file_stops)
df_calendar = pd.read_csv(file_calendar)

"""
creation of the metro trips dataset
"""
df_mode_metro = df_mode[df_mode["mode"]=="M"]
df_metro_id_str= df_mode_metro.numero_lig.astype(str)
df_routes_metro = df_routes[df_routes.route_short_name.isin(df_metro_id_str)]

df_metro_trips = df_trips[df_trips.route_id.isin(df_routes_metro.route_id)]
df_metro_trips = df_metro_trips.drop(["trip_headsign", "block_id", "shape_id"], axis=1)

print(df_metro_trips.head())

"""
filtering the calendar dataset in week, saturday, sunday
"""
# df_metro_trips = pd.join()
col = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']

df_calendar["week"] = df_calendar['monday']*df_calendar['tuesday']*df_calendar['wednesday']*df_calendar['thursday']*df_calendar['friday']
df_calendar.drop(['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'start_date', 'end_date'], inplace=True, axis=1)

print(df_calendar.head())

"""
joining calendar and metro trip
"""

df_metro_trip_calendar = pd.merge(df_metro_trips, df_calendar, on="service_id")
print(df_metro_trip_calendar)


"""
merging stop_times and metro_trip_calendar
"""
df_stop_times.drop(["pickup_type", "drop_off_type"], inplace=True, axis=1)
df_metro_time = pd.merge(df_metro_trip_calendar, df_stop_times, on="trip_id")
print(df_metro_time )
print(df_metro_time.stop_id.unique())
print(len(df_metro_time.stop_id.unique()))

# for i in range(len(df_metro_time)):
#     if df_metro_time.stop_id[i] == 8743:
#         pass

# df_metro_time["headway"] = df_metro_time.arrival_time.apply(lambda x: )



