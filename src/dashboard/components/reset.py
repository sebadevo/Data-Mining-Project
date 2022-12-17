from dash import Dash, html, dcc,ctx
import dash
import plotly.express as px
from utils import *
from dash.dependencies import Output, Input, State
from . import ids
from utils import get_interval, remove_duplicates, find_match_V2, map_to_sec, get_headway, interval_score, stop_score
import plotly.graph_objects as go


# from preprocessing import compute_time_difference, convert_dataframe_to_time_sorted
import pandas as pd
from database.load_db import get_connection

from time import process_time
import warnings
warnings.simplefilter(action='ignore', category=UserWarning)


def render(app: Dash) -> html.Div:
    @app.callback(
                Output(ids.DAY, "value"),
                Output(ids.DATE, "value"),
                Output(ids.REAL_DATE, "value"),
                Input('reset', 'n_clicks'),
                prevent_initial_call=True
                )
    def reset_all(click): 
        return (None, None, None) if ctx.triggered_id == "reset" else dash.no_update            

    return  html.Button("Reset", id = "reset")