from dash import Dash, dcc, ctx
from dash.dependencies import Output, Input, State

import pandas as pd
import datetime

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
aliases_2 = {"CIM. DE BRUXELLES":"CIM. BRUXELLES"}

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
                    State(ids.DIRECTION_1, 'value'), 
                    State(ids.DIRECTION_2, 'value')],
                    prevent_initial_call=True
        )
    def enable_dropdown_stop(line_name, dir_left, dir_right): 
        return ctx.triggered_id is None and line_name is None

    @app.callback(
                Output(ids.STOP, 'options'),
                [State(ids.SELECTED_LINE,'data'),
                State(ids.DIRECTION_1, 'value'),
                State(ids.DIRECTION_2, 'value'),
                Input(ids.DIRECTION_1,"className"),
                Input(ids.DIRECTION_2,"className"),
                ], prevent_initial_call=True
    )
    def query_route_short_name(line_name, dir_left, dir_right,left_class,right_class):
        print("starting")
        direction = ""
        if "direction--inactive" in left_class: 
            direction = dir_right
        elif "direction--inactive" in right_class: 
            direction = dir_left
        if direction in aliases_2:
            direction =  aliases_2[direction]
        print(direction)
        query = (
            "select distinct tr.direction_id, tr.trip_headsign"
            " from trips tr" 
            " inner join routes ro on tr.route_id = ro.routes_id"
            " where ro.route_type = %s and ro.routes_short_name = %s and  tr.trip_headsign = %s" # how do I use direction in this SQL querry ????
            )
        connection = get_connection()
        print(pd.read_sql(query, params=[which_type(line_name), line_name, direction], con= connection)) #direction
        direction = int(pd.read_sql(query, params=[which_type(line_name), line_name, direction], con= connection).iat[0,0])  
        print(direction)      
        query = (
            "select distinct CONCAT(st.stop_id,' - ',s.stop_name) as stops, st.stop_sequence "
            " from trips tr" 
            " inner join routes ro on tr.route_id = ro.routes_id"
            " inner join stop_times st on st.trip_id = tr.trip_id"
            " inner join stops s on s.stop_id = st.stop_id"
            " where ro.route_type = %s and ro.routes_short_name = %s and tr.direction_id = %s" 
            " order by st.stop_sequence ASC"
            )
        data = pd.read_sql(query, params=[which_type(line_name), line_name, direction], con= connection)
        return data.stops.unique().tolist()
    return dcc.Dropdown(
                id="stop-name",
                multi=False,
                disabled=True,
                clearable=False,
                className='form-dropdown drop',
                placeholder="Select the stop",
                persistence="numeric",
                persistence_type='memory'
                )


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
                placeholder="Select the day", 
                persistence_type='memory') #To check ? 

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
            "select distinct c.monday, c.saturday, c.sunday, CONCAT(c.start_date,' - ',c.end_date) as date"
            " from trips tr" 
            " inner join routes ro on tr.route_id = ro.routes_id"
            " inner join stop_times st on st.trip_id = tr.trip_id"
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

        # data['date'] = data[["start_date", "end_date"]].apply(lambda x: ' - '.join(x.astype(str)), axis=1)
                
        return data.date.unique().tolist()

    return dcc.Dropdown(
                id="date-name",
                clearable=False,
                className='form-dropdown drop',
                disabled=True,
                placeholder="Select the date",
                persistence_type='memory') 


# # --------------------SPECIFIC DATE DROPDOWN--------------------
# # --------------------------------------------------------------

def real_date_render(app: Dash):
    @app.callback(
            Output(ids.REAL_DATE, "disabled"),
            Input(ids.DATE,'value'),
            prevent_initial_call=True
    )
    def enable_dropdown_stop(date): 
        return not date

    @app.callback(
                    Output(ids.REAL_DATE, 'options'), 
                    [
                    Input(ids.DATE, 'value'), 
                    State(ids.DAY, 'value')
                    ], prevent_initial_call=True
        )
    def get_specific_date(date, day_type):
        start_date, end_date = date.split(" - ")
        start_year, start_month, start_day = int(start_date[:4]), int(start_date[4:6]), int(start_date[6:])
        end_year, end_month, end_day = int(end_date[:4]), int(end_date[4:6]), int(end_date[6:])
        start_date = datetime.date(start_year, start_month, start_day)
        end_date = datetime.date(end_year, end_month, end_day)
        delta = datetime.timedelta(days=1)
        dates = []
        while start_date <= end_date:
            day_value = start_date.weekday()
            date = "".join(str(start_date).split("-"))
            if day_value  < 5 and day_type == "Weekday":
                if day_value == 0:
                    day = "Monday"
                elif day_value == 1:
                    day = "Tuesday"
                elif day_value == 2:
                    day = "Wednesday"
                elif day_value == 3:
                    day = "Thursday"
                elif day_value == 4:
                    day = "Friday"
                dates.append(f"{date} - {day}")
            elif day_value  == 5 and day_type == "Saturday":
                day = "Saturday"
                dates.append(f"{date} - {day}")
            elif day_value  == 6 and day_type == "Sunday":
                day = "Sunday"
                dates.append(f"{date} - {day}")
            start_date += delta
        return dates

    return dcc.Dropdown(
                id="real-date-name",
                clearable=False,
                className='form-dropdown drop',
                disabled=True,
                placeholder="Select the date for the real data",
                persistence_type='memory') 