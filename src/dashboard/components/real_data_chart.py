from dash import Dash, html, dcc
import plotly.express as px
from utils import *
from dash.dependencies import Output, Input, State
from . import ids
from utils import get_interval

from preprocessing import compute_time_difference, convert_dataframe_to_time_sorted, real_data_processing
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

def render(app: Dash) -> html.Div:
    @app.callback(
            Output(ids.REAL_DATA_CHART, "children"),
            State(ids.STOP, 'value'),
            Input(ids.DATE, 'value'),
            State(ids.DAY, 'value'),
            State(ids.SELECTED_LINE,'data'),
            prevent_initial_call=True
            )
    def update_bar_chart(stop_name,date_name,day_name, line_name) -> html.Div:  
        stop_name = stop_name.split(' - ')[0]
        query = (
            "select time, lineID, pointID, date"
            " from real_data" 
            " where lineID = %s and pointID = %s and date >= %s and date <=  %s"
            )
        connection = get_connection()
        start_time = process_time()
        data = pd.read_sql(query, params=[line_name, stop_name, int(which_date(date_name)[0]), int(which_date(date_name)[1])], con= connection)
        print(f"The time taken is {process_time() - start_time}")
        data.rename(columns={'time':'arrival_time'}, inplace=True)
        if( len(data) < 5):
            return html.Div(html.H4(f"There is not enough data to plot a graph (number of lines in the data is: {len(data)})"))
        
        # data = real_data_processing()
        data = convert_dataframe_to_time_sorted(data)

        x,y = compute_time_difference(data)

        lines = get_interval(x,y)

        def create_data(x,y):
            data = pd.DataFrame()
            data["x"] = x
            data["y"] = y
            return data

        data = create_data(x,y)
        fig = px.bar(data,x="x",y="y")
        fig.update_traces(width=0.05)

        for i in range(len(lines)-1):
            beg = x.index(lines[i])
            end = x.index(lines[i+1])
            if i != len(lines)-2:
                end -= 1

            average = mean(y[beg:end])
            if average > 12 :
                fig.add_shape(type="rect",
                    x0=x[beg]-0.05, y0=0, x1=x[end]+0.05 , y1=max(y[beg:end])+1.5,
                line=dict(color='red'))
            else :
                fig.add_shape(type="rect",
                    x0=x[beg]-0.05, y0=0, x1=x[end]+0.05 , y1=mean(y[beg:end])+3,
                line=dict(color='green'))
        return html.Div([html.H4("Real Data"),dcc.Graph(figure=fig)], id=ids.REAL_DATA_CHART)
    return html.Div(id=ids.REAL_DATA_CHART)


