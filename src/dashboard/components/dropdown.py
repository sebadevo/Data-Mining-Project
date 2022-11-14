from dash import Dash, html, dcc
import plotly.express as px
from dashboard.enumeration import Type,Day

from dash.dependencies import Output, Input
from . import ids

from database.load_db import load_dataframe
from preprocessing import load_data_and_merge,filter,compute_time_difference,retrieve_info_title
import pandas as pd


def mode_render():
    return dcc.Dropdown(
                ["Bus","Tram","Metro"],
                id="mode",
                multi=False,
                clearable=False,
                className='form-dropdown drop',
                placeholder="Select the mode",
                persistence="string")

def line_name_render(app: Dash):
    @app.callback(
                Output('line-name', "disabled"),
                [Input('mode','value')])
    def enable_dropdown(mode):  
        return mode in ["Metro","Tram"]        

    return dcc.Dropdown(
                options = ["Bus","Tram","hoho"],
                id="line-name",
                multi=False,
                clearable=False,
                className='form-dropdown drop',
                placeholder="Select the line",
                persistence="string")