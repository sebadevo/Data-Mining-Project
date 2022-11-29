from dash import Dash, dcc

from dash.dependencies import Output, Input

import pandas as pd

from database.load_db import get_connection




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
        print("debug", line_name)
        return data.stop_desc.tolist()

    return dcc.Dropdown(
                # options = ["Bus","Tram","Metro"],
                id="stop-name",
                multi=False,
                clearable=False,
                className='form-dropdown drop',
                placeholder="Select the stop",
                persistence="numeric")

# --------------------DIRECTION_ID DROPDOWN------------------------------
# ------------------------------------------------------------------

def direction_id_render(app: Dash):
    @app.callback(
                Output('dir-name', "disabled"),
                [Input('stop-name','value')]
    )
    def enable_dropdown_stop(stop_name): 
        # print("debug line_name", len(stop_name), type(stop_name)) 
        return len(stop_name) ==0
    
    @app.callback(
                Output('dir-name', 'options'), 
                [Input('mode', 'value'), 
                Input('line-name','value'), 
                Input('stop-name', 'value')]
    )

    def query_route_short_name(mode, line_name, stop_name):
        line_name = line_name.split(' - ')[0]
        stop_name = stop_name.split(' - ')[0]
        query = (
            "select st.stop_id,ro.routes_short_name, ro.routes_long_name, s.stop_name, tr.direction_id, tr.trip_headsign"
            " from trips tr" 
            " inner join routes ro on tr.route_id = ro.routes_id"
            " inner join stop_times st on st.trip_id = tr.trip_id"
            " inner join stops s on s.stop_id = st.stop_id"
            " where ro.route_type = %s and ro.routes_short_name = %s and st.stop_id = %s"
            )
        connection = get_connection()
        data = pd.read_sql(query, params=[mode, line_name, stop_name ], con= connection)
        data['dir_desc'] = data[["direction_id", "trip_headsign"]].apply(lambda x: ' - '.join(x.astype(str)), axis=1)
        #print("DEBUGGING: \n", data.dir_desc)

        return data.dir_desc.unique().tolist()

    return dcc.Dropdown(
                # options = ["Bus","Tram","Metro"],
                id="dir-name",
                multi=False,
                clearable=False,
                className='form-dropdown drop',
                placeholder="Select the direction",
                persistence="string") #To check ? 


# --------------------DAY DROPDOWN------------------------------
# ------------------------------------------------------------------



# def day_render():
#     return dcc.Dropdown(
#                 options=[{"label": "weekday", "value" : "1"},{"label":"Saturday", "value":"2"}, {"label": "Sunday", "value":"3"}],
#                 id="day-name",
#                 multi=False,
#                 clearable=False,
#                 className='form-dropdown drop',
#                 placeholder="Select the mode",
#                 persistence="string")

def day_render(app: Dash):
    @app.callback(
                Output('day-name', "disabled"),
                [Input('dir-name','value')]
    )
    def enable_dropdown_stop(dir_name): 
        # print("debug line_name", len(stop_name), type(stop_name)) 
        return len(dir_name) ==0
    
    @app.callback(
                Output('day-name', 'options'), 
                [Input('mode', 'value'), 
                Input('line-name','value'), 
                Input('stop-name', 'value'), 
                Input('dir-name', 'value')]
    )

    def query_route_short_name(mode, line_name, stop_name, dir_name):
        line_name = line_name.split(' - ')[0]
        stop_name = stop_name.split(' - ')[0]
        dir_name = dir_name.split(' - ')[0]

        query = (
            "select st.stop_id,ro.routes_short_name, ro.routes_long_name, s.stop_name, tr.direction_id, tr.trip_headsign, c.monday, c.saturday, c.sunday"
            " from trips tr" 
            " inner join routes ro on tr.route_id = ro.routes_id"
            " inner join stop_times st on st.trip_id = tr.trip_id"
            " inner join stops s on s.stop_id = st.stop_id"
            " inner join calendar c on c.service_id = tr.service_id"
            " where ro.route_type = %s and ro.routes_short_name = %s and st.stop_id = %s and tr.direction_id = %s"
            )
        connection = get_connection()
        data = pd.read_sql(query, params=[mode, line_name, stop_name, dir_name], con= connection)

        data.rename(columns={'monday' : "weekday"}, inplace=True)

        data["days"] = data[['weekday', 'saturday', 'sunday']].apply(lambda x: x.weekday*100 + x.saturday*10 + x.sunday)
        print("Debugging days : ", data.days.unique())


        # data['dir_desc'] = data[["direction_id", "trip_headsign"]].apply(lambda x: ' - '.join(x.astype(str)), axis=1)
        # print("DEBUGGING: \n", data.dir_desc)

        return data.days.unique().tolist()

    return dcc.Dropdown(
                # options = ["Bus","Tram","Metro"],
                id="day-name",
                multi=False,
                clearable=False,
                className='form-dropdown drop',
                placeholder="Select the day",
                persistence="string") #To check ? 