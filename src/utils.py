import pandas as pd
from math import floor, ceil
from statistics import mean

def time_to_sec(time:str):
    """converts a string time format into an int seconds format.

    Args:
        time (str): Time should follow the convention : "hours:minutes:seconds".
        Example : "23:45:12" will output 85512.

    Returns:
        int: The time in seconds.
    """
    time = time.split(":")
    hours, minutes, seconds = int(time[0]), int(time[1]), int(time[2])
    if hours < 5:
        return 86400 + hours*60*60+minutes*60+seconds
    return hours*60*60+minutes*60+seconds

def get_times(direction:int, weekday:int, route_short_name:str, stop_id:str, start_date:int, dataframe:pd.DataFrame):
    """generates a list of all the arrival time at a stop station given *All arguments*.

    Args:
        direction (int): the direction the transport is heading to
        weekday (int): the day of the week.
        route_short_name (str): the name of the tram/bus/metro.
        stop_id (str): the stop identification.
        start_date (int): the weekdate
        dataframe (pd.DataFrame): the dataframe containing all the data.

    Returns:
        list: the list of all the arrival times at a given stop station.
    """
    data = dataframe.loc[(dataframe['direction_id'] == direction) & (dataframe['weekday'] == weekday) & (dataframe['route_short_name'] == route_short_name) & (dataframe['stop_id'] == stop_id)  & (dataframe['start_date'] == start_date)]
    return data['arrival_time'].tolist()

def map_to_min(arrival_times:list):
    """transfroms the arrival times, which is a list of str of time, into a sorted list of the times in minutes.

    Args:
        arrival_times (list): list of string of the arrival times.

    Returns:
        list: list of int of the arrival times in minutes.
    """
    arrival_times_minutes = map(time_to_sec, arrival_times)
    arrival_times_minutes = list(arrival_times_minutes)
    return sorted(arrival_times_minutes)

def get_headway(arrival_times_minutes):
    """generates a headway.

    Args:
        arrival_times_minutes (list): list of the arrival times in minutes at a stop.

    Returns:
        tuple(list, list): returns the time associated with each headway. (the times of the day are in x, the headway are in y)
    """
    x, y = [], []
    for i in range(len(arrival_times_minutes)-1):
        y.append(round((arrival_times_minutes[i+1]-arrival_times_minutes[i])/60, 2))
        x.append(round(arrival_times_minutes[i]/3600, 2))
    return x, y

def gradient(y):
    """computes a special gradient to detect when there are variation in the headway.

    Args:
        y (list): list of int, the headway.

    Returns:
        list: list of boolean (int values, 0 or 1) indicating if (1) their is a variation or (0) there are no variation.
    """
    output = []
    for i in range(len(y)-1):
        value = y[i+1]-y[i]
        if value:
            output.append(1)
        else:
            output.append(0)
    output.append(1)
    return output


def get_interval(x, y):
    """detects the interval in a given headway

    Args:
        x (list): the time associated to a headway.
        y (list): the headway associated to a time.

    Returns:
        list: list of the time corresponding to the intervals.

    """
    index = i = 0
    y = gradient(y)
    lines = [x[0]]
    
    while i < len(y):
        mode = check_mode(y, i)
        start = index

        if mode == "diff": 
            i, index = diff_mode(y, start, i, index)
        elif mode == "zero":
            i, index = zero_mode(y, start, i, index)

        i, index = check_index(i, index, y)
        lines.append(x[index])
            
    if x[-1] not in lines:
        lines.append(x[-1])

    return lines

def check_mode(y, i, distance=7, threshold=4):
    return "zero" if sum(y[i:i+distance]) < threshold else "diff"

def diff_mode(y, start, i, index):
    count_zeros = 0
    temp = 0
    while (count_zeros < 4 or start + 4 > index) and i < len(y): # creating the diff zone
        if y[i]:
            if temp >= 2:
                count_zeros = 0
                temp = 0
            elif count_zeros:
                temp+=1
        elif index != i:
            if not count_zeros:
                index = i
            count_zeros += 1
        i+=1   
    return i, index

def zero_mode(y, start, i, index):
    count_diff = 0
    temp = 0
    while (count_diff < 1 or start + 4 > index) and i < len(y):
        if y[i]: 
            if not count_diff:
                index = i
            count_diff += 1
        elif temp > 2:
            count_diff = 0
            temp = 0
        elif count_diff:
            temp +=1
        i+=1
    return i, index

def check_index(i, index, y):
    if index > len(y) - 4:
            index = len(y)-1
            i = index + 1
    elif i < len(y):
        i = index + 1
    else:
        index = len(y)-1
    return i, index

def mean_filter(y, k=3):
    output = [y[:floor(k/2)]] 
    output.extend(mean(y[i-floor(k/2):i+floor(k/2)]) for i in range(floor(k/2), len(y)-floor(k/2)))
    output.append(y[len(y)-floor(k/2):])
    return output

def get_categories(x, y, intervals):
    categories = []
    length = len(intervals)-1
    for i in range(length):
        beg = x.index(intervals[i])
        end = x.index(intervals[i+1])

        if i != length-1:
            end -= 1
            
        average = mean(y[beg:end])
        cat = 'P' if average > 12 else 'R'

        categories.append(cat)

    return categories


def load_data():
    routes_data = pd.read_csv('../../data/gtfs23Sept/routes.csv', sep=",")
    trips_data = pd.read_csv('../../data/gtfs23Sept/trips.csv', sep=",")
    stop_times_data = pd.read_csv('../../data/gtfs23Sept/stop_times.csv', sep=",")
    calendar_data = pd.read_csv('../../data/gtfs23Sept/calendar.csv', sep=",")
    return routes_data, trips_data, stop_times_data, calendar_data

def get_arrival_time(routes_data, trips_data, stop_times_data, calendar_data, 
                     route_type, direction, day, route_short_name, stop_id, start_date):
    trips_routes_merge = pd.merge(trips_data, routes_data, on='route_id')
    trips_routes_merge = trips_routes_merge[['trip_id', 'service_id', 'route_type', 'route_short_name', 'trip_headsign', 'direction_id']]
    trips_routes_merge = trips_routes_merge.loc[trips_routes_merge['route_type'] == route_type]
    trips_routes_calendar = pd.merge(trips_routes_merge, calendar_data, on='service_id')
    
    trips_routes_calendar.drop(['end_date', 'tuesday', 'wednesday', 'thursday', 'friday', 'service_id'], inplace=True, axis=1)
    trips_routes_calendar.rename(columns={'monday': 'weekday'}, inplace=True)
    dataframe = pd.merge(stop_times_data, trips_routes_calendar, on='trip_id',how="inner")
    dataframe.drop(['pickup_type', 'drop_off_type', 'stop_sequence', 'departure_time'], inplace=True, axis=1)
    data = dataframe.loc[(dataframe['direction_id'] == direction) & (dataframe['weekday'] == 1) & (dataframe['route_short_name'] == route_short_name) & (dataframe['stop_id'] == stop_id)  & (dataframe['start_date'] == start_date)]
    return data['arrival_time'].tolist(), data

def sec_to_time(time:int):
    hours = time//3600
    minutes = (time % 3600)//60
    seconds = time % 60
    return f'{hours}:{minutes}:{seconds}'
