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
                options=[{"label": "Tram", "value" : "0"},{"label":"Metro", "value":"1"}, {"label": "Bus", "value":"3"}],
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
        return mode not in ["0","1", "3"]  

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

        data['name'] = data.iloc[:,:2].apply(lambda x: ' - '.join(x.astype(str)), axis=1)
        return data.name.tolist()

    return dcc.Dropdown(
                # options = ["Bus","Tram","Metro"],
                id="line-name",
                multi=False,
                clearable=False,
                className='form-dropdown drop',
                placeholder="Select the line",
                persistence="string")

# --------------------STOP_ID DROPDOWN------------------------------
# ------------------------------------------------------------------

def stop_id_render(app: Dash):
    @app.callback(
                Output('stop-name', "disabled"),
                [Input('line-name','value')]
    )
    def enable_dropdown_stop(line_name): 
        print("debug line_name", len(line_name), type(line_name)) 
        return len(line_name) ==0
    
    @app.callback(
                Output('stop-name', 'options'), 
                [Input('mode', 'value'), 
                Input('line-name','value')]
    )

    def query_route_short_name(mode, line_name):
        line_name = line_name.split(' - ')[0]
        query = (
            "select st.stop_id,ro.routes_short_name, ro.routes_long_name, s.stop_name"
            " from trips tr" 
            " inner join routes ro on tr.route_id = ro.routes_id"
            " inner join stop_times st on st.trip_id = tr.trip_id"
            " inner join stops s on s.stop_id = st.stop_id"
            " where ro.route_type = %s and ro.routes_short_name = %s"
            )
        connection = get_connection()
        data = pd.read_sql(query, params=[mode, line_name], con= connection)
        data['stop_desc'] = data[["stop_id", "stop_name"]].apply(lambda x: ' - '.join(x.astype(str)), axis=1)
        # print("debug", mode)
        return data.stop_desc.tolist()

    return dcc.Dropdown(
                # options = ["Bus","Tram","Metro"],
                id="stop-name",
                multi=False,
                clearable=False,
                className='form-dropdown drop',
                placeholder="Select the stop",
                persistence="numeric")