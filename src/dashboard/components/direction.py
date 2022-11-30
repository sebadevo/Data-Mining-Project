from dash import Dash, html
from dash.dependencies import Output, Input
import dash
from . import ids



import pandas as pd
import numpy as np
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

def render(app : Dash):
    @app.callback(
        Output('dir-1',"className"),
        Output('dir-2', "className"),
        Output('dir-1',"disabled"),
        Output('dir-2', "disabled"),
        [Input('dir-1','n_clicks'),
        Input('dir-2','n_clicks')]
    )
    def enable_dropdown_stop(*clicks): 
        if "1" in dash.callback_context.triggered_id:
            return  "direction direction--2 v navigable", "direction direction--2 f direction--inactive navigable", True,False
        if "2" in dash.callback_context.triggered_id:
            return  "direction direction--2 v direction--inactive navigable", "direction direction--2 f navigable", False,True
        return "direction direction--2 v direction--inactive navigable", "direction direction--2 f navigable", False,True

    @app.callback(
        Output('directions-container', 'children'),
        Input(ids.SELECTED_LINE, 'data'),
        )
    def change_button(value):
        query = (
            "select routes_long_name"
            " from routes" 
            " where route_type = %s and routes_short_name = %s"
            )
        connection = get_connection()
        data = pd.read_sql(query, params=[which_type(value), value ], con= connection)
        headsign = data.routes_long_name.tolist()[0].split("-")
        return [html.Div([html.Button([headsign[0].strip()], className="direction direction--2 v direction--inactive navigable", disabled=False, id="dir-1", tabIndex="0")], className="direction-container"), html.Div([html.Button([headsign[1].strip()], className="direction direction--2 f navigable", id="dir-2", disabled=True, tabIndex="0")], className="direction-container")]


    return html.Div([
        html.Div([
            html.Button(["Simonis"],className="direction direction--2 v direction--inactive navigable" ,disabled=False,id='dir-1',tabIndex="0"),
        ],className="direction-container"),
        html.Div([
            html.Button(["Elisabeth"],className="direction direction--2 f navigable" ,id='dir-2',disabled=True,tabIndex="0"),
        ],className="direction-container"),
    ],  
        className="directions-container",
        id="directions-container"
    )
        
def generate_left_button():
    pass


def generate_right_button():
    pass