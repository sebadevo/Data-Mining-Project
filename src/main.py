from preprocessing import load_data_and_merge,filter,compute_time_difference,retrieve_info_title
from plotting import plot_schedulde_headways



def show_schedulde_headways(direction_id, saterday, stop_id, short_name, start_date):
    route = 'data/gtfs3Sept/routes.csv'
    trips = 'data/gtfs3Sept/trips.csv'
    stop_times = 'data/gtfs3Sept/stop_times.csv'
    calendar = 'data/gtfs3Sept/calendar.csv'
    data = load_data_and_merge(route,trips,stop_times,calendar)
    data = filter(data, direction_id= direction_id, saterday=saterday, stop_id=stop_id,short_name= short_name,start_date= start_date)
    x,y = compute_time_difference(data)
    print(data)
    trip_headsign, long_name, stop_name = retrieve_info_title(data,stop_id=stop_id)
    plot_schedulde_headways(x,y,line=short_name,line_name=long_name,trip_headsign=trip_headsign,stop_name=stop_name)






