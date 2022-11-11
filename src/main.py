from preprocessing import load_data_and_merge,filter,compute_time_difference,retrieve_info_title
from plotting import plot_schedulde_headways
from enumeration import Type,Day



def show_schedulde_headways(type, day, direction_id, stop_id, short_name, start_date):
    route = 'data/gtfs3Sept/routes.csv'
    trips = 'data/gtfs3Sept/trips.csv'
    stop_times = 'data/gtfs3Sept/stop_times.csv'
    calendar = 'data/gtfs3Sept/calendar.csv'
    data = load_data_and_merge(type,route,trips,stop_times,calendar)
    data = filter(data, day = day,direction_id= direction_id,stop_id=stop_id,short_name= short_name,start_date= start_date)
    x,y = compute_time_difference(data)
    trip_headsign, long_name, stop_name = retrieve_info_title(data,stop_id=stop_id)
    plot_schedulde_headways(x,y,line=short_name,line_name=long_name,trip_headsign=trip_headsign,stop_name=stop_name,type = type)



if __name__ == "__main__":
    show_schedulde_headways(type = Type.Tram,day= Day.Saterday,direction_id =0, stop_id= '5705', short_name = '3', start_date= 20210911)


