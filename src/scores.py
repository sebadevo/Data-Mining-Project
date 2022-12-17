from utils import *
# from utils import get_interval, remove_duplicates, find_match_V2, map_to_sec, get_headway, interval_score, stop_score
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

import pandas as pd
from database.load_db import get_connection

import warnings
warnings.simplefilter(action='ignore', category=UserWarning)
from time import process_time


metro = ["1","2","5","6"]
tram = ["3","4","7","8","9","19","25","39","44","51","55","62","81","82","92","93","97"]
bus = ["12","13","14","T19","20","21","27","28","29","33","34","36","37","38",
    "41","42","43","45","46","47","48","49","50","52","53","54","56","57","58","59","60","61","63",
    "64","65","66","69","70","71","72","73","74","75","76","77","78","79","80","T81","T82","83","86","87","88","89","90","T92","95"]
noctis = ["04","05","06","08","09","10","11","12","13","16","18"]

def which_type(value):
    if value in metro:
        return 1
    return 0 if value in tram else 3

def which_date(value): 
    return value.split(" - ")

def which_day(value): 
    Weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    return "Weekday" if value in Weekdays else value


#INput : Selected_line (route_id, line_id), Stop (stop_id), DATE (start_date), REAL_DATE (date)


#IN THE DATASET WE WANT: line ((routes)routes_short_name, (top_times) stop_id, real_date (date))

def get_data(theoric:bool, type_: int):
    connection = get_connection()

    if theoric: 
        query = ( 
                "select ro.routes_short_name, st.stop_id, c.start_date, c.end_date"
                " from trips tr"
                " inner join routes ro on tr.route_id = ro.routes_id" 
                " inner join stop_times st on tr.trip_id = st.trip_id" 
                " inner join calendar c on c.service_id = tr.service_id"
                " where c.start_date >= 20210906 and ro.route_type = %s"
                )
        return pd.read_sql(query,  params=[type_], con= connection)
    else: 
        query = ( 
                "select rd.date, rd.pointID, rd.lineID, rd.distanceFromPoint"
                " from real_data rd"
                )
        return pd.read_sql(query, con= connection)




def compute_score(line_name, stop_name, real_date_name,date ) : 

    # print( "the date: ", real_date, "and", type(real_date)) 

    day = which_day(findDay(real_date_name))
    real_date_name = str(real_date_name)

    if (which_type(line_name) == 1): #For metros
        query = ( 
            "select rd.time"
            " from real_data rd" 
            " where rd.lineID = %s and rd.pointID = %s and rd.date = %s and rd.distanceFromPoint <= 1"
            )
        
    elif (which_type(line_name) == 0): #For trams
        query = ( 
            "select rd.time"
            " from real_data rd" 
            " where rd.lineID = %s and rd.pointID = %s and rd.date = %s and rd.distanceFromPoint <= 100"
            )

    elif (which_type(line_name) == 3): #for buses
        query = ( 
            "select rd.time"
            " from real_data rd" 
            " where rd.lineID = %s and rd.pointID = %s and rd.date = %s and rd.distanceFromPoint <= 100"
            )

    connection = get_connection()
    real_data = pd.read_sql(query, params=[line_name,stop_name,real_date_name], con= connection)

    if len(real_data)>5: 
        query = (
            "select st.arrival_time, c.monday, c.saturday, c.sunday"
            " from trips tr" 
            " inner join routes ro on tr.route_id = ro.routes_id"
            " inner join stop_times st on st.trip_id = tr.trip_id"
            " inner join calendar c on c.service_id = tr.service_id"
            " where ro.route_type = %s and ro.routes_short_name = %s and st.stop_id = %s and c.start_date = %s and c.end_date = %s"
            )
        connection = get_connection()
        # print("waht is wrong: ", which_type(line_name), line_name, stop_name, int(which_date(date)[0]), int(which_date(date)[1]))
        data = pd.read_sql(query, params=[which_type(line_name), line_name, stop_name, int(which_date(date)[0]), int(which_date(date)[1])], con= connection)
        if len(data)>5: 
        # print("The theoretical data size is: ", data.shape)

            time_real = map_to_sec(real_data.time.tolist())
            time_th = map_to_sec(data.arrival_time.tolist())

            time_real = remove_duplicates(time_real)

            x,y = get_headway(time_th)
            intervals = get_interval(x,y)
            categories = get_categories(x, y, intervals)

            if (len(time_th) < len(time_real)): 
                scheduled_times, real_times = find_match_V2(time_th, time_real)
            else: 
                real_times, scheduled_times = find_match_V2(time_real, time_th)


            real_headways_x,real_headways_y = get_headway(real_times)
            scheduled_headways_x,scheduled_headways_y = get_headway(scheduled_times)
            qualities = interval_score(scheduled_times, real_times, scheduled_headways_x, real_headways_x, scheduled_headways_y, real_headways_y, intervals, categories)


            return round(stop_score(qualities, intervals, day)*100, 3)
        else: 
            return None
    else: 
        return None

#---------------------------------------------METRO--------------------------------------

# theoric_data = get_data(True, 1)
# print("this is the theoric data size: ", theoric_data.shape)
# theoric_data['date'] = theoric_data[["start_date", "end_date"]].apply(lambda x: ' - '.join(x.astype(str)), axis=1)
# # print("Got the theorical data")
# real_data = get_data(False, 1)
# # print("Got the real_data: ", real_data.shape)
# column_names = ["Line", "Stop", "Date", "Real_date", "Score"]
# stop_score_data = pd.DataFrame(columns= column_names)


# stops = theoric_data.theoric_data.stop_id.unique()
# dates = theoric_data.date.unique()
# real_dates = real_data.date.unique()
# # f = open("myOutFile.txt", "a")
            
# for line in metro: 
#     for stop in stops: 
#         for date in dates: 
#             for real_date in real_dates: 
#                 # f.write(f"{line}--{stop}--{real_date}--{date}\n")
#                 score = compute_score(line, stop, real_date, date)
#                 if score is not None: 
#                     values=[line, stop, date, real_date, score]
#                     new_row = pd.Series(dict(zip(column_names, values)))
#                     stop_score_data = pd.concat([stop_score_data, new_row.to_frame().T], ignore_index=True)

# stop_score_data.to_csv("metro_scores.csv", index=False)


# print("FININSHED WITH THE METRO")



#---------------------------------------------TRAM--------------------------------------

theoric_data = get_data(True, 0)
print("this is the theoric data size: ", theoric_data.shape)
theoric_data['date'] = theoric_data[["start_date", "end_date"]].apply(lambda x: ' - '.join(x.astype(str)), axis=1)
# print("Got the theorical data")
real_data = get_data(False, 0)
# print("Got the real_data: ", real_data.shape)
column_names = ["Line", "Stop", "Date", "Real_date", "Score"]
stop_score_data = pd.DataFrame(columns= column_names)
# f = open("myOutFile.txt", "a")
stops = theoric_data.theoric_data.stop_id.unique()
dates = theoric_data.date.unique()
real_dates = real_data.date.unique()
# f = open("myOutFile.txt", "a")
            
for line in metro: 
    for stop in stops: 
        previous_time = process_time()
        for date in dates: 
            for real_date in real_dates: 
                if real_date >= which_date(real_date)[0] and real_date <= which_date(real_date)[1]:
                # f.write(f"{line}--{stop}--{real_date}--{date}\n")
                    score = compute_score(line, stop, real_date, date)
                    if score is not None: 
                        values=[line, stop, date, real_date, score]
                        new_row = pd.Series(dict(zip(column_names, values)))
                        stop_score_data = pd.concat([stop_score_data, new_row.to_frame().T], ignore_index=True)
        print(f"The time taken is: {process_time()-previous_time}s")


stop_score_data.to_csv("tram_scores.csv", index=False)

print("FININSHED WITH THE TRAM")


theoric_data = get_data(True, 3)
print("this is the theoric data size: ", theoric_data.shape)
theoric_data['date'] = theoric_data[["start_date", "end_date"]].apply(lambda x: ' - '.join(x.astype(str)), axis=1)
# print("Got the theorical data")
real_data = get_data(False, 3)
# print("Got the real_data: ", real_data.shape)
column_names = ["Line", "Stop", "Date", "Real_date", "Score"]
stop_score_data = pd.DataFrame(columns= column_names)
# f = open("myOutFile.txt", "a")
            
stops = theoric_data.theoric_data.stop_id.unique()
dates = theoric_data.date.unique()
real_dates = real_data.date.unique()
# f = open("myOutFile.txt", "a")
            
for line in metro: 
    for stop in stops: 
        for date in dates: 
            for real_date in real_dates: 
                # f.write(f"{line}--{stop}--{real_date}--{date}\n")
                score = compute_score(line, stop, real_date, date)
                if real_date >= which_date(real_date)[0] and real_date <= which_date(real_date)[1]:
                # f.write(f"{line}--{stop}--{real_date}--{date}\n")
                    score = compute_score(line, stop, real_date, date)
                    if score is not None: 
                        values=[line, stop, date, real_date, score]
                        new_row = pd.Series(dict(zip(column_names, values)))
                        stop_score_data = pd.concat([stop_score_data, new_row.to_frame().T], ignore_index=True)



stop_score_data.to_csv("bus_scores.csv", index=False)


print("FININSHED WITH THE BUS")
