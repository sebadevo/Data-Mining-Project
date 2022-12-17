import pandas as pd
from math import floor, ceil
from statistics import mean
import datetime
import calendar

weekday_weights  = [4, 1, 0, 0, 0, 0, 20, 71, 100, 64, 35, 47, 61, 61, 66, 76, 64, 84, 76, 64, 48, 33, 20, 11]
saturday_weights = [11, 1, 0, 0, 0, 3, 8, 14, 23, 32, 40, 46, 50, 52, 54, 57, 61, 62, 58, 49, 36, 26, 24, 23]
sunday_weights   = [1, 0, 0, 0, 0, 0, 4, 10, 17, 25, 33, 39, 44, 46, 47, 49, 51, 51, 47, 40, 30, 20, 11, 5]

Weights = {"Weekday":weekday_weights, "Saturday":saturday_weights, "Sunday":sunday_weights}

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
    # print("checking2: ", hours)
    if hours < 4:
        return 86400 + hours*3600+minutes*60+seconds
    return hours*3600+minutes*60+seconds


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


def map_to_sec(arrival_times:list):
    """transfroms the arrival times, which is a list of str of time, into a sorted list of the times in minutes.

    Args:
        arrival_times (list): list of string of the arrival times.

    Returns:
        list: list of int of the arrival times in minutes.
    """
    arrival_times_minutes = map(time_to_sec, arrival_times)
    arrival_times = list(arrival_times_minutes)
    return sorted(arrival_times)


def get_headway(arrival_times):
    """generates a headway.

    Args:
        arrival_times (list): list of the arrival times in seconds at a stop.

    Returns:
        tuple(list, list): returns the time associated with each headway. 
                           (the times of the day in hours are in x, the headway in miniutes are in y)
    """
    x, y = [], []
    for i in range(len(arrival_times)-1):
        y.append(round((arrival_times[i+1]-arrival_times[i])/60, 2))
        x.append(round(arrival_times[i]/3600, 2))
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
        beg = get_closest_index(x, intervals[i], intervals[i], intervals[i+1])
        end = get_closest_index(x, intervals[i+1], intervals[i], intervals[i+1])
        if beg is not None  and end is not None :
            if beg < end:
                average = mean(y[beg:end])
                cat = 'P' if average > 12 else 'R'
            else: 
                cat = None
        else: 
            cat = None
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


def remove_duplicates(real, threshold=45):
    i = len(real)-1
    while i > 0:
        if real[i] - threshold < real[i-1]:
            real.pop(i)
        i -= 1
    return real


def find_match_V1(short, long):
    shorted_index = []
    j = 0
    for i in range(len(short)):
        index = 0
        dist = 9999
        for t in range(6):
            a = min(max(0, j+t), len(long)-1)
            if a not in shorted_index and abs(short[i]-long[a]) < dist:
                dist = abs(short[i]-long[a])
                index = a
        j = index 
        shorted_index.append(j)
        j+=1
    shorted = sorted([long[i] for i in shorted_index])
    return short, shorted


def find_match_V2(short, long):
    index_short_list = []
    index_long_list = []
    while len(index_short_list) < len(short):
        column = []
        for i in range(len(short)):
            if i not in index_short_list:
                min_value = 99999
                index_short = i
                index_long = 1
                for j in range(len(long)):
                    if j not in index_long_list and abs(long[j] - short[i]) < min_value:
                        min_value = abs(long[j]-short[i])
                        index_short = i
                        index_long = j
                column.append([min_value, index_short, index_long])
        for item in column:
            index_long = item[2]
            if index_long not in index_long_list:
                index_short = item[1]
                min_value = item[0]
                for item_ in column:
                    if item_[2] == index_long and min_value > item_[0]:
                        min_value = item_[0]
                        index_short = item_[1]
                index_short_list.append(index_short)
                index_long_list.append(index_long)

    to_sort = [long[i] for i in index_long_list]
    shortened = sorted(to_sort)

    return short, shortened


def punctuality(scheduled_times, real_times):
    time_diffs = [abs(scheduled_times[i]-real_times[i]) for i in range(len(scheduled_times))]
    quality_index = 1 - (mean(time_diffs) / (12*60))
    return max(0, quality_index)


def regularity(scheduled_headways, real_headways):
    if not len(scheduled_headways) or not len(real_headways): 
        return 0
    awt = sum(h**2 for h in real_headways) / (2*sum(real_headways))
    swt = sum(h**2 for h in scheduled_headways) / (2*sum(scheduled_headways))
    ewt = abs(awt - swt)
    quality_index = 1 - (ewt/swt)
    return max(0, quality_index)


def harmonic_mean(qualities):
    return 1/sum(1/quality for quality in qualities)

def stop_score(qualities, interval, day, precision=60):
    """computes the score for a given stop. 
    The length of the interval list should be 1 greater then of qualities.

    Args:
        qualities (list): list of scores between 0 and 1 representing the quality for a time frame (associeted to the intervals).
        interval (list): list of int containing the interval for each quality score.
        day (str): The day it represents (either Weekday, Saturday or Sunday).
        precision (int): The precision of the measures. A higher number leads to a higher precision. A precision of 1 is equal to a quality per hour,
                         60 to a quality per minute, 3600 to a quality per second. Default is 60.
    return:
        score (int): score between 0 and 1 representing the quality at a stop.
    """
    if day in Weights:
        weights = Weights[day]
    else: 
        print(f"the day received is not in the available days : {list(Weights.keys())}. day received =", day)
        return 0
    if len(qualities) != len(interval) -1:
        print("the qualities and interval don't correspond. qualities = ", qualities, "interval = ", interval)
        return 0

    interval = [i*precision for i in interval] # preperation variables
    values = 24*precision
    adjusted_qualities = []
    length = len(qualities)
    j = 0

    for i in range(max(ceil(interval[-1]), values)): # converting the quality to a one to one match with time with the required precision.
        if j < length:
            if i < interval[0]:
                adjusted_qualities.append(0)
            elif interval[j] <= i < interval[j+1]:
                adjusted_qualities.append(qualities[j])
            elif i >= interval[j+1]:
                j+=1
                if j < length:
                    adjusted_qualities.append(qualities[j])
                else:
                    adjusted_qualities.append(0)
        else:
            adjusted_qualities.append(0)

    for i in range(len(adjusted_qualities)-values): # adjusting the time from [0,R] to [0,values - 1]
        adjusted_qualities[i] = adjusted_qualities[i+values]
    adjusted_qualities = adjusted_qualities[:values]
    weights = [weights[floor(i/precision)] for i in range(values)]

    # compute the integral of the scalar product betwen adjusted_qualities and weights divided by integral of wieghts
    score = sum(q * w for q, w in zip(adjusted_qualities, weights))/sum(weights)
    return round(score,4)


def interval_score(scheduled_times, real_times, scheduled_headways_x, real_headways_x, scheduled_headways_y, real_headways_y, intervals, categories):
    """computes the score for each interval based on the average headway. If the average headway is over 12 minutes, then the 
    poncutality metric will be used, otherwise the regularity metric will be used. (refer to get_categories for more details).

    Args:
        schedule_times (list): list of the scheduled times in seconds.
        real_times (list): list of the real arrival times at a stop in seconds.
        scheduled_headways_x (list): list of scheaduled_headways on x axis in hours.
        scheduled_headways_y (list): list of scheaduled_headways on y axis in minutes.
        real_headways_x (list): list of real_headways on x axis in hours.
        real_headways_y (list): list of real_headways on y axis in minutes.
        interval (list): list of times seperating each interval in which to compute the metrics.
        categories (list): list of the string (either "P" or "R") corresponding to the metric that should be applied to an interval .
    
    return:
        qualities (list): list of (int) quality for each interval.
    """
    qualities = []
    length = len(intervals)-1
    for i in range(length):
        beg = get_closest_index(scheduled_headways_x, intervals[i], intervals[i], intervals[i+1])
        end = get_closest_index(scheduled_headways_x, intervals[i+1], intervals[i], intervals[i+1])
        if beg is not None  and end is not None :
            if beg >= end: 
                score =0
            elif categories[i] == "P":
                end += 1
                score = punctuality(scheduled_times[beg:end], real_times[beg:end])
            elif categories[i] == "R":
                score = regularity(scheduled_headways_y[beg:end], real_headways_y[beg:end])
        else: 
            score=0
        qualities.append(score)
    return qualities


def get_closest_index(elements: list, value: int, beg: int, end:int) -> int: 

    if (value != end and value in elements) or value == elements[-1] : # we want to get the interval [ elem[i], elem[i+1] [ but if we have the last elem then we accept the [ elem[i], elem[i+1] ]
        return elements.index(value)

    dist = 99999
    index = None
    for i in range(len(elements)):
        if beg < elements[i] < end and abs(elements[i] - value) < dist:
            index = i
            dist = abs(elements[i] -value)
        elif elements[i] > end: 
            break
    
    return index

def findDay(date):
    date = str(date)
    year, month, day = int(date[:4]), int(date[4:6]), int(date[6:])
    day = datetime.date(year, month, day)
    return day.strftime("%A")
    




def get_specific_date(date, day_type):
        start_date, end_date = date.split(" - ")
        start_year, start_month, start_day = int(start_date[:4]), int(start_date[4:6]), int(start_date[6:])
        end_year, end_month, end_day = int(end_date[:4]), int(end_date[4:6]), int(end_date[6:])
        start_date = datetime.date(start_year, start_month, start_day)
        end_date = datetime.date(end_year, end_month, end_day)
        delta = datetime.timedelta(days=1)
        dates = []
        while start_date <= end_date:
            day_value = start_date.weekday()
            date = "".join(str(start_date).split("-"))
            if day_value  < 5 and day_type == "Weekday":
                if day_value == 0:
                    day = "Monday"
                elif day_value == 1:
                    day = "Tuesday"
                elif day_value == 2:
                    day = "Wednesday"
                elif day_value == 3:
                    day = "Thursday"
                elif day_value == 4:
                    day = "Friday"
                dates.append(f"{date} - {day}")
            elif day_value  == 5 and day_type == "Saturday":
                day = "Saturday"
                dates.append(f"{date} - {day}")
            elif day_value  == 6 and day_type == "Sunday":
                day = "Sunday"
                dates.append(f"{date} - {day}")
            start_date += delta
        return dates