from preprocessing import load_data_and_merge,filter,compute_time_difference,retrieve_info_title
from plotting import plot_schedulde_headways
from dashboard.enumeration import Type,Day
from database.load_db import load_dataframe
from time import process_time
from utils import get_interval
from statistics import mean

def show_schedulde_headways(type, day, direction_id, stop_id, short_name, start_date):  
    start_time = process_time()
    data = load_dataframe(day,type.value,direction_id =direction_id, stop_id= stop_id, short_name = short_name, start_date= start_date)
    time_taken = process_time() - start_time
    print(data.columns)
    print(f"Time taken for the database is {time_taken}")
    x,y = compute_time_difference(data)
    intervals = get_interval(x, y)
    print(intervals)
    trip_headsign, long_name, stop_name = retrieve_info_title(data,stop_id=stop_id)

    plot_schedulde_headways(x,y,line=short_name,line_name=long_name,trip_headsign=trip_headsign, intervals=intervals, stop_name=stop_name,type = type)



if __name__ == "__main__":
    show_schedulde_headways(type = Type.Tram,day= Day.Saterday, direction_id =0, stop_id= '5705', short_name = '3', start_date= 20210911)


