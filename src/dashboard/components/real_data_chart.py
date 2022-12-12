from dash import Dash, html, dcc
import plotly.express as px
from utils import *
from dash.dependencies import Output, Input, State
from . import ids
from utils import get_interval, remove_duplicates, find_match_V2

from preprocessing import compute_time_difference, convert_dataframe_to_time_sorted
import pandas as pd
from database.load_db import get_connection

from time import process_time
import warnings
warnings.simplefilter(action='ignore', category=UserWarning)

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

def draw_fig(data, intervals, x, y): 

    fig = px.bar(data,x="x",y="y")
    fig.update_traces(width=0.05)   

    for i in range(len(intervals)-1):

        beg = get_closest_index(x, intervals[i], intervals[i], intervals[i+1])
        end = get_closest_index(x, intervals[i+1], intervals[i], intervals[i+1])
        average = mean(y[beg:end])

        if average > 12 :
            fig.add_shape(type="rect",
                x0=intervals[i]-0.05, y0=0, x1=intervals[i+1]-0.05 , y1=max(y[beg:end])+1.5,
            line=dict(color='red'))

        else :
            fig.add_shape(type="rect",
                x0=intervals[i]-0.05, y0=0, x1=intervals[i+1]-0.05 , y1=mean(y[beg:end])+3,
            line=dict(color='green'))

    return fig

def render(app: Dash) -> html.Div:
    @app.callback(
            Output(ids.REAL_DATA_CHART, "children"),
            State(ids.SELECTED_LINE,'data'),
            State(ids.STOP, 'value'),
            State(ids.DATE, 'value'),
            Input(ids.REAL_DATE, 'value'),
            prevent_initial_call=True
            )

    def update_bar_chart(line_name, stop_name,date, real_date_name ) -> html.Div:  
        stop_name = stop_name.split(' - ')[0]
        real_date_name = real_date_name.split('-')[0]
        if (which_type(line_name) == 1): #For metros
            query = ( 
                "select rd.time"
                " from real_data rd" 
                " where rd.lineID = %s and rd.pointID = %s and rd.date = %s and rd.distanceFromPoint =0"
                )


        elif (which_type(line_name) == 0): #For trams
            query = ( 
                "select rd.time"
                " from real_data rd" 
                " where rd.lineID = %s and rd.pointID = %s and rd.date = %s and rd.distanceFromPoint < 50"
                )
        else : 
            return html.Div(html.H4("This feature has not been implemented yet, would you kindly select a line from a metro and go on as if nothing happened ? \n"
            "from the developpers team."))
        connection = get_connection()
        start_time = process_time()
        real_data = pd.read_sql(query, params=[line_name, stop_name, real_date_name], con= connection)
        query = (
            "select st.arrival_time, c.monday, c.saturday, c.sunday"
            " from trips tr" 
            " inner join routes ro on tr.route_id = ro.routes_id"
            " inner join stop_times st on st.trip_id = tr.trip_id"
            " inner join stops s on s.stop_id = st.stop_id"
            " inner join calendar c on c.service_id = tr.service_id"
            " where ro.route_type = %s and ro.routes_short_name = %s and st.stop_id = %s and c.start_date = %s and c.end_date = %s"
            )
        connection = get_connection()
        data = pd.read_sql(query, params=[which_type(line_name), line_name, stop_name, int(which_date(date)[0]), int(which_date(date)[1])], con= connection)
        # print(f"The time taken is {process_time() - start_time}")

        if( len(real_data) < 5):
            return html.Div(html.H4(f"There is not enough data to plot a graph (number of lines in the data is: {len(real_data)})"))
        
        
        time_real = map_to_sec(real_data.time.tolist())
        time_th = map_to_sec(data.arrival_time.tolist())


        time_real = remove_duplicates(time_real)

        x,y = get_headway(time_th)
        intervals = get_interval(x,y)

        if (len(time_th) < len(time_real)): 
            scheduled_times, real_times = find_match_V2(time_th, time_real)
        else: 
            real_times, scheduled_times = find_match_V2(time_real, time_th)



        real_headways_x,real_headways_y = get_headway(real_times)
        scheduled_headways_x,scheduled_headways_y = get_headway(scheduled_times)

        def create_data(x,y):
            data = pd.DataFrame()
            data["x"] = x
            data["y"] = y
            return data

        scheduled_data = create_data(scheduled_headways_x,scheduled_headways_y )

        real_data = create_data(real_headways_x,real_headways_y )


        fig_real = draw_fig(real_data, intervals, real_headways_x, real_headways_y)
        fig_scheduled = draw_fig(scheduled_data, intervals, scheduled_headways_x, scheduled_headways_y)
        
        return html.Div([html.A("Real Data"),dcc.Graph(figure=fig_real),html.A("Scheduled Headway After Match"),dcc.Graph(figure=fig_scheduled) ], className="metric-plot", id=ids.REAL_DATA_CHART)
    return html.Div(id=ids.REAL_DATA_CHART)


