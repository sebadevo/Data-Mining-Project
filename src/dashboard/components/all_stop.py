import dash_bootstrap_components as dbc
from dash import Dash, html ,dcc, Input, Output, State
from database.load_db import get_connection
import pandas as pd
import numpy as np

metro = ["1","2","5","6"]
tram = ["3","4","7","8","9","19","25","39","44","51","55","62","81","82","92","93","97"]
bus = ["12","13","14","T19","20","21","27","28","29","33","34","36","37","38",
    "41","42","43","45","46","47","48","49","50","52","53","54","56","57","58","59","60","61","63",
    "64","65","66","69","70","71","72","73","74","75","76","77","78","79","80","T81","T82","83","86","87","88","89","90","T92","95"]
noctis = ["04","05","06","08","09","10","11","12","13","16","18"]

def render(app : Dash):
    def which_type(value):
        if value in metro:
            return 1
        return 0 if value in tram else 3

    @app.callback(
    Output('all_stops', 'children'),
    Input('actual_line', 'data'),
    )
    def display_output(value):
        if value == 0:
           return html.A("No line seleted")
        print("debugging :", which_type(value),"  ",value)
        query = (
            "select s.stop_name"
            " from trips tr" 
            " inner join routes ro on tr.route_id = ro.routes_id"
            " inner join stop_times st on st.trip_id = tr.trip_id"
            " inner join stops s on s.stop_id = st.stop_id"
            " where ro.route_type = %s and ro.routes_short_name = %s"
            )
        connection = get_connection()
        data = pd.read_sql(query, params=[which_type(value), value], con= connection)
        return html.A(" - ".join(np.unique(data.stop_name.tolist())))

    return html.Div([
    ],  
    id="all_stops"
    )
    