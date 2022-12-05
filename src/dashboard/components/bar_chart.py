from dash import Dash, html, dcc
import plotly.express as px
from dashboard.enumeration import Type,Day
from utils import *
from dash.dependencies import Output, Input
from . import ids
from utils import get_interval

from database.load_db import load_dataframe
from preprocessing import load_data_and_merge,filter,compute_time_difference,retrieve_info_title
import pandas as pd
from database.load_db import get_connection



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

def render(app: Dash) -> html.Div:
    @app.callback(
            Output(ids.BAR_CHART, "children"),
            [Input(ids.SELECTED_LINE,'data'), 
            Input(ids.STOP, 'value'),
            Input(ids.DATE, 'value'),
            Input(ids.DAY, 'value'),
            ])
    def update_bar_chart(line_name, stop_name,date_name,day_name) -> html.Div:  
        # print("the args list: ", which_type(line_name), line_name, stop_name, int(which_date(date_name)[0]), int(which_date(date_name)[1]))
        stop_name = stop_name.split(' - ')[0]
        query = (
            "select st.stop_id, st.arrival_time, st.departure_time, ro.routes_short_name, ro.routes_long_name, s.stop_name, tr.direction_id, tr.trip_headsign, c.monday, c.saturday, c.sunday, c.start_date, c.end_date"
            " from trips tr" 
            " inner join routes ro on tr.route_id = ro.routes_id"
            " inner join stop_times st on st.trip_id = tr.trip_id"
            " inner join stops s on s.stop_id = st.stop_id"
            " inner join calendar c on c.service_id = tr.service_id"
            " where ro.route_type = %s and ro.routes_short_name = %s and st.stop_id = %s and c.start_date = %s and c.end_date = %s"
            )
        connection = get_connection()
        data = pd.read_sql(query, params=[which_type(line_name), line_name, stop_name, int(which_date(date_name)[0]), int(which_date(date_name)[1])], con= connection)
        if day_name == "Weekday": 
            data = data[data.monday == 1]
        elif day_name == "Saturday": 
            data = data[data.saturday == 1]
        else: 
            data = data[data.sunday == 1]
        print("checking: ", data.head())
        x,y = compute_time_difference(data)
        lines = get_interval(x,y)

        def create_data(x,y):
            data = pd.DataFrame()
            data["x"] = x
            data["y"] = y
            return data, lines

        data, lines = create_data(x,y)
        # def load_data(type = Type.Tram,day= Day.Saterday, direction_id =0, stop_id= '5705', short_name = '3', start_date= 20210911):
        #     data = load_dataframe(day,type.value,direction_id =direction_id, stop_id= stop_id, short_name = short_name, start_date= start_date)
        #     x,y = compute_time_difference(data)
        #     lines = get_interval(x, y)
        #     data = pd.DataFrame()
        #     data["x"] = x
        #     data["y"] = y
        #     print(data)
        #     return data, lines

        # if mode not in ["0","1","3"] :
        #     return html.Div("chey",id=ids.BAR_CHART)
        # data, lines = load_data(type = Type.Tram,day= Day.Saterday, direction_id =0, stop_id= '5705', short_name = '3', start_date= 20210911)
        fig = px.line(data,x="x",y="y")
        for line in lines:
            fig.add_vline(x = line, line_color = 'red')


        return html.Div(dcc.Graph(figure=fig), id=ids.BAR_CHART)

    return html.Div(id=ids.BAR_CHART)


