from dash import Dash, html, dcc
import plotly.express as px
from utils import *
from dash.dependencies import Output, Input, State
from . import ids
from utils import get_interval, remove_duplicates, find_match_V2, map_to_sec, get_headway, interval_score, stop_score
import plotly.graph_objects as go
import folium


# from preprocessing import compute_time_difference, convert_dataframe_to_time_sorted
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


def get_data():
    query = (
            "select distinct tr.direction_id"
            " from trips tr" 
            " inner join routes ro on tr.route_id = ro.routes_id"
            " where ro.route_type = %s and ro.routes_short_name = %s and  tr.trip_headsign = %s" # how do I use direction in this SQL querry ????
            )
    connection = get_connection()
    direction = pd.read_sql(query, params=[], con= connection)        
        
def create_map():
    stib_map = folium.Map(
        location=[50.8476, 4.3572],
        zoom_start=12,
        # tiles = 'MapBox Bright'
        # tiles = 'Stamen Terrain'
        # tiles = 'Stamen Toner'
        # tiles='cartodbdark_matter'
        tiles='cartodbpositron'
    )

    stib_map.save('map_save.html')


def display_map(line):
    return html.Div([
        html.A('Interactive STIB Map'),
        html.Iframe(id=ids.MAP, srcDoc=open(f'src/map/stib_map_{line}.html', 'r').read(), width='100%', height='600')
    ])

def display_map_score(date):
    return html.Div([
        html.A('Interactive STIB Map'),
        html.Iframe(id=ids.MAP, srcDoc=open(f'src/map/stib_score_map_{date}.html', 'r').read(), width='100%', height='600')
    ])
    
def display_all_map():
    return html.Div([html.A('Interactive STIB Map'), html.Iframe(id=ids.MAP, srcDoc=open('src/map/stib_map.html', 'r').read(), width='100%', height='600')], id=ids.ALL_MAP)
