from preprocessing import load_data_and_merge,filter,compute_time_difference,retrieve_info_title
from plotting import plot_schedulde_headways
from dashboard.enumeration import Type,Day
from database.load_db import load_dataframe
from time import process_time
from utils import get_interval, time_to_sec, sec_to_time
from statistics import mean
from database.load_db import get_connection
import pandas as pd

def show_schedulde_headways(type, day, direction_id, stop_id, short_name, start_date):  
    # start_time = process_time()
    data = load_dataframe(day,type.value,direction_id =direction_id, stop_id= stop_id, short_name = short_name, start_date= start_date)
    # data['arrival_time'].tolist()
    # time_taken = process_time() - start_time
    # print(data.columns)
    # print(f"Time taken for the database is {time_taken}")
    # x,y = compute_time_difference(data)
    # intervals = get_interval(x, y)
    # print(intervals)
    #trip_headsign, long_name, stop_name = retrieve_info_title(data,stop_id=stop_id)
    print(data['arrival_time'])
    return data['arrival_time'].tolist()
    # plot_schedulde_headways(x,y,line=short_name,line_name="blajbalj",trip_headsign="bobo", intervals=intervals, stop_name='hihi',type = type)


def real_data_processing(date, lineID, pointID, distanceFromPoint, duplicates):
    query = (
            "select rd.time"
            " from real_data rd" 
            " where rd.date = %s and rd.lineID = %s and rd.pointID = %s and rd.distanceFromPoint <= %s"
            )
    connection = get_connection()
    data = pd.read_sql(query, params=[date, lineID, pointID, distanceFromPoint], con= connection)
    print(data[4:15])
    return data['time'].tolist()

def remove_duplicates(real):
    i = len(real)-1
    while i > 0:
        if real[i] - 45 < real[i-1]:
            real.pop(i)
        i -= 1
    return real

def find_match_drop(real_times, scheduled_times):
    shorted = []
    j = 0
    for i in range(len(real_times)):
        index = 0
        dist = 9999999
        for t in range(6):
            if abs(real_times[i]-scheduled_times[min(max(0, j+t), len(scheduled_times)-1)]) < dist:
                dist = abs(real_times[i]-scheduled_times[min(max(0, j+t), len(scheduled_times)-1)])
                index = min(max(0, j+t), len(scheduled_times)-1)
        j = index 
        shorted.append(scheduled_times[j])
        j+=1
    return real_times, shorted


if __name__ == "__main__":
    real_time = real_data_processing(date=20210908, lineID=1, pointID=8081, distanceFromPoint=0, duplicates=1)
    predict_time = show_schedulde_headways(type = Type.Metro,day= Day.Weekday, direction_id =1, stop_id= '8081', short_name = '1', start_date= 20210901)
    # x,y = compute_time_difference(predict_time)
    real_time = sorted(map(time_to_sec, real_time))
    predict_time = sorted(map(time_to_sec, predict_time))
    # print(real_time)
    # print(predict_time)
    print("real_time is :")
    real_time = remove_duplicates(real_time)
    temp_real, temp_theory = find_match_drop(real_time, predict_time)
    real_time = list(map(sec_to_time,real_time))
    print(real_time)
    print("the length of the real data is:", len(real_time))
    print("############################")
    print("theorical time is :")
    predict_time = list(map(sec_to_time,predict_time))
    print(predict_time)
    print("the length of the theoritical data is:", len(predict_time))

    print("###################################################")
    print("##########comparaison with same length#############")
    print("###################################################")
    
    temp_real = list(map(sec_to_time,temp_real))
    temp_theory = list(map(sec_to_time,temp_theory))
    print(temp_real)
    print(temp_theory)
    print(len(temp_real))
    print(len(temp_theory))



    
    
