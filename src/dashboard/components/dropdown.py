from dash import Dash, dcc, ctx
from dash.dependencies import Output, Input, State

import pandas as pd

from database.load_db import get_connection
from time import process_time
from . import ids

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

# --------------------STOP_ID DROPDOWN------------------------------
# ------------------------------------------------------------------

def stop_id_render(app: Dash):
    @app.callback(
                    Output(ids.STOP, "disabled"),
                    [Input(ids.SELECTED_LINE,'data'), 
                    Input(ids.DIRECTION_1, 'value'), 
                    Input(ids.DIRECTION_2, 'value')],
                     prevent_initial_call=True
        )
    def enable_dropdown_stop(line_name, dir_left, dir_right): 
        button_clicked = ctx.triggered_id
        if button_clicked == ids.DIRECTION_1: 
            print("the chosen line is: ", line_name, "\nThe chosen left dir is: ", dir_left)
        elif button_clicked == ids.DIRECTION_2: 
            print("the chosen line is: ", line_name, "\nThe chosen right dir is: ", dir_right)            
        return button_clicked is None and line_name is None

    @app.callback(
                Output(ids.STOP, 'options'),
                [Input(ids.SELECTED_LINE,'data'),
                Input(ids.DIRECTION_1, 'value'),
                Input(ids.DIRECTION_2, 'value')
                ], prevent_initial_call=True
    )

    def query_route_short_name(line_name, dir_left, dir_right):
        button_clicked = ctx.triggered_id
        direction = ""
        if button_clicked == ids.DIRECTION_1: 
            direction = dir_left
        elif button_clicked == ids.DIRECTION_2: 
            direction = dir_right
        query = (
            "select st.stop_id,ro.routes_short_name, ro.routes_long_name, s.stop_name"
            " from trips tr" 
            " inner join routes ro on tr.route_id = ro.routes_id"
            " inner join stop_times st on st.trip_id = tr.trip_id"
            " inner join stops s on s.stop_id = st.stop_id"
            " where ro.route_type = %s and ro.routes_short_name = %s" # how do I use direction in this SQL querry ????
            )
        connection = get_connection()
        start_time = process_time()
        data = pd.read_sql(query, params=[which_type(line_name), line_name], con= connection)
        data['stop_desc'] = data[["stop_id", "stop_name"]].apply(lambda x: ' - '.join(x.astype(str)), axis=1)
        data = data[data['routes_long_name'].str.contains(direction)] #NECESSARY ???????
        print(f"Time for the query is {process_time() - start_time}")
        return data.stop_desc.tolist()
    return dcc.Dropdown(
                id="stop-name",
                multi=False,
                disabled=True,
                clearable=False,
                className='form-dropdown drop',
                placeholder="Select the stop",
                persistence="numeric")


# # --------------------DAY DROPDOWN------------------------------
# # --------------------------------------------------------------


def day_render(app: Dash):
    @app.callback(
                    Output(ids.DAY, "disabled"),
                    Input(ids.STOP,'value'),
                     prevent_initial_call=True
        )
    def enable_dropdown_stop(stop): 
        return not stop
    @app.callback(
        Output(ids.DAY, 'options'), 
        [
        Input(ids.STOP, 'value')
        ], prevent_initial_call=True
        )
    def query_date_name(stop):               
        return ["Weekday", "Saturday", "Sunday"]
    return dcc.Dropdown(["Weekday", "Saturday", "Sunday"],
                id="day-name",
                disabled=True,
                clearable=False,
                className='form-dropdown drop',
                placeholder="Select the day") #To check ? 

# # --------------------DATE DROPDOWN-----------------------------
# # --------------------------------------------------------------

def date_render(app: Dash):
    @app.callback(
            Output(ids.DATE, "disabled"),
                Input(ids.DAY,'value'),
                    prevent_initial_call=True
    )
    def enable_dropdown_stop(day): 
        return not day

    @app.callback(
                    Output(ids.DATE, 'options'), 
                    [
                    State(ids.SELECTED_LINE,'data'), 
                    State(ids.STOP, 'value'), 
                    Input(ids.DAY, 'value')
                    ], prevent_initial_call=True
        )
    def query_date_name(line_name, stop_name, day_name):
        stop_name = stop_name.split(' - ')[0]
        query = (
            "select st.stop_id,ro.routes_short_name, ro.routes_long_name, s.stop_name, tr.direction_id, tr.trip_headsign, c.monday, c.saturday, c.sunday, c.start_date, c.end_date"
            " from trips tr" 
            " inner join routes ro on tr.route_id = ro.routes_id"
            " inner join stop_times st on st.trip_id = tr.trip_id"
            " inner join stops s on s.stop_id = st.stop_id"
            " inner join calendar c on c.service_id = tr.service_id"
            " where ro.route_type = %s and ro.routes_short_name = %s and st.stop_id = %s"
            )
        connection = get_connection()
        data = pd.read_sql(query, params=[which_type(line_name), line_name, stop_name], con= connection)

        if day_name == "Weekday": 
            data = data[data.monday == 1]
        elif day_name == "Saturday": 
            data = data[data.saturday == 1]
        else: 
            data = data[data.sunday == 1]

        data['date'] = data[["start_date", "end_date"]].apply(lambda x: ' - '.join(x.astype(str)), axis=1)
                
        return data.date.unique().tolist()

    return dcc.Dropdown(
                id="date-name",
                clearable=False,
                className='form-dropdown drop',
                disabled=True,
                placeholder="Select the date",) 