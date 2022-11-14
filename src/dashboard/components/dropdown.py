from dash import Dash, html, dcc
import plotly.express as px
from dashboard.enumeration import Type,Day

from dash.dependencies import Output, Input
from . import ids

from database.load_db import load_dataframe
from preprocessing import load_data_and_merge,filter,compute_time_difference,retrieve_info_title
import pandas as pd

from database.load_db import get_connection, close_connection




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
        return mode not in ["Metro","Tram", "Bus"]  

    @app.callback(
                Output('line-name', 'options'), 
                [Input('mode','value')]
    )
    def query_route_short_name(mode):
        query = (
            "select routes_short_name,  routes_long_name from routes where route_type = %s;"
            )
        connection = get_connection()
        data = pd.read_sql(query, params=[mode], con= connection)

        data['name'] = data.iloc[:,:2].apply(lambda x: ','.join(x.astype(str)), axis=1)
        return data.name.tolist()

    return dcc.Dropdown(
                options = ["Bus","Tram","hoho"],
                id="line-name",
                multi=False,
                clearable=False,
                className='form-dropdown drop',
                placeholder="Select the line",
                persistence="string")
    