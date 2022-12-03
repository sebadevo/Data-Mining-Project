from dash import Dash, dcc, html


from dash.dependencies import Output, Input

import pandas as pd

from database.load_db import get_connection

from . import ids
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
# day_render, stop_render, date_render


# def mode_render():
#     return dcc.Dropdown(
#                 options=[{"label": "Tram", "value" : "0"},{"label":"Metro", "value":"1"}, {"label": "Bus", "value":"3"}],
#                 id="mode",
#                 multi=False,
#                 clearable=False,
#                 className='form-dropdown drop',
#                 placeholder="Select the mode",
#                 persistence="string")

# def line_name_render(app: Dash):
#     @app.callback(
#                 Output('line-name', "disabled"),
#                 [Input('mode','value')])
#     def enable_dropdown(mode):  
#         return mode not in ["0","1", "3"]  

#     @app.callback(
#                 Output('line-name', 'options'), 
#                 [Input('mode','value')]
#     )
#     def query_route_short_name(mode):
#         query = (
#             "select routes_short_name,  routes_long_name from routes where route_type = %s;"
#             )
#         connection = get_connection()
#         data = pd.read_sql(query, params=[mode], con= connection)

#         data['name'] = data.iloc[:,:2].apply(lambda x: ' - '.join(x.astype(str)), axis=1)
#         return data.name.tolist()

#     return dcc.Dropdown(
#                 # options = ["Bus","Tram","Metro"],
#                 id="line-name",
#                 multi=False,
#                 clearable=False,
#                 className='form-dropdown drop',
#                 placeholder="Select the line",
#                 persistence="string")

# --------------------STOP_ID DROPDOWN------------------------------
# ------------------------------------------------------------------

def stop_id_render(app: Dash):
    @app.callback(
                Output('stop-name', "disabled"),
                [Input(ids.SELECTED_LINE,'data'), 
                Input(ids.DIRECTION_1, 'data'), 
                Input(ids.DIRECTION_2, 'data')]
    )
   

    def enable_dropdown_stop(line_name, dir_left, dir_right): 
        print("the chosen line is: ", line_name, "\nThe chosen dir is: ", dir_left, dir_right)
        return len(line_name) !=0 #test
    
    @app.callback(
                Output('stop-name', 'options'), #Input('mode', 'value'), 
                [Input(ids.SELECTED_LINE,'data'),
                Input(ids.DIRECTION_1, 'value'),
                Input(ids.DIRECTION_2, 'value')
                ]
    )

    def query_route_short_name(line_name, dir_left, dir_right):
        query = (
            "select st.stop_id,ro.routes_short_name, ro.routes_long_name, s.stop_name"
            " from trips tr" 
            " inner join routes ro on tr.route_id = ro.routes_id"
            " inner join stop_times st on st.trip_id = tr.trip_id"
            " inner join stops s on s.stop_id = st.stop_id"
            " where ro.route_type = %s and ro.routes_short_name = %s"
            )
        connection = get_connection()
        data = pd.read_sql(query, params=[which_type(line_name), line_name ], con= connection)
        data['stop_desc'] = data[["stop_id", "stop_name"]].apply(lambda x: ' - '.join(x.astype(str)), axis=1)
        return data.stop_desc.tolist()


    # def query_route_short_name(mode, line_name):
    #     line_name = line_name.split(' - ')[0]
    #     query = (
    #         "select st.stop_id,ro.routes_short_name, ro.routes_long_name, s.stop_name"
    #         " from trips tr" 
    #         " inner join routes ro on tr.route_id = ro.routes_id"
    #         " inner join stop_times st on st.trip_id = tr.trip_id"
    #         " inner join stops s on s.stop_id = st.stop_id"
    #         " where ro.route_type = %s and ro.routes_short_name = %s"
    #         )
    #     connection = get_connection()
    #     data = pd.read_sql(query, params=[mode, line_name], con= connection)
    #     data['stop_desc'] = data[["stop_id", "stop_name"]].apply(lambda x: ' - '.join(x.astype(str)), axis=1)
    #     print("debug", line_name)
    #     return data.stop_desc.tolist()

    return dcc.Dropdown(
                # options = ["Bus","Tram","Metro"],
                id="stop-name",
                multi=False,
                clearable=False,
                className='form-dropdown drop',
                placeholder="Select the stop",
                persistence="numeric")


# # --------------------DAY DROPDOWN------------------------------
# # --------------------------------------------------------------


def day_render(app: Dash):
    @app.callback(
                Output('day-name', "disabled"),
                [Input('stop-name','data')]
    )
    def enable_dropdown_stop(stop_name): 
        return len(stop_name) ==0
    
    @app.callback(
                Output('day-name', 'options'), 
                [# Input('mode', 'value'), 
                Input('line-name','data'), 
                Input('stop-name', 'data'), 
                # Input('dir-name', 'value')
                ]
    )

    def query_route_short_name(line_name, stop_name):
        # line_name = line_name.split(' - ')[0]
        stop_name = stop_name.split(' - ')[0]
        # dir_name = dir_name.split(' - ')[0]

        query = (
            "select st.stop_id,ro.routes_short_name, ro.routes_long_name, s.stop_name, tr.direction_id, tr.trip_headsign, c.monday, c.saturday, c.sunday"
            " from trips tr" 
            " inner join routes ro on tr.route_id = ro.routes_id"
            " inner join stop_times st on st.trip_id = tr.trip_id"
            " inner join stops s on s.stop_id = st.stop_id"
            " inner join calendar c on c.service_id = tr.service_id"
            " where ro.route_type = %s and ro.routes_short_name = %s and st.stop_id = %s"
            )
        connection = get_connection()
        data = pd.read_sql(query, params=[line_name, stop_name], con= connection)

        data.rename(columns={'monday' : "weekday"}, inplace=True)


        data["days"] = data.apply(lambda x: x.weekday*100 + x.saturday*10 + x.sunday, axis=1)

        data.days.replace([100, 10, 1], ["Weekday", "Saturday", "Sunday"], inplace=True)
        return data.days.unique().tolist()

    return dcc.Dropdown(
                # options=[{"label": "Weekday", "value" : 100},{"label":"Saturday", "value":10}, {"label": "Sunday", "value":1}],
                id="day-name",
                multi=False,
                clearable=False,
                className='form-dropdown drop',
                placeholder="Select the day",
                style={"margin-left": "25px"},
                persistence="string") #To check ? 

# --------------------DIRECTION_ID DROPDOWN------------------------------
# ------------------------------------------------------------------

# def direction_id_render(app: Dash):
#     @app.callback(
#                 Output('dir-name', "disabled"),
#                 [Input('stop-name','value')]
#     )
#     def enable_dropdown_stop(stop_name): 
#         # print("debug line_name", len(stop_name), type(stop_name)) 
#         return len(stop_name) ==0
    
#     @app.callback(
#                 Output('dir-name', 'options'), 
#                 [Input('mode', 'value'), 
#                 Input('line-name','value'), 
#                 Input('stop-name', 'value')]
#     )

#     def query_route_short_name(mode, line_name, stop_name):
#         line_name = line_name.split(' - ')[0]
#         stop_name = stop_name.split(' - ')[0]
#         query = (
#             "select st.stop_id,ro.routes_short_name, ro.routes_long_name, s.stop_name, tr.direction_id, tr.trip_headsign"
#             " from trips tr" 
#             " inner join routes ro on tr.route_id = ro.routes_id"
#             " inner join stop_times st on st.trip_id = tr.trip_id"
#             " inner join stops s on s.stop_id = st.stop_id"
#             " where ro.route_type = %s and ro.routes_short_name = %s and st.stop_id = %s"
#             )
#         connection = get_connection()
#         data = pd.read_sql(query, params=[mode, line_name, stop_name ], con= connection)
#         data['dir_desc'] = data[["direction_id", "trip_headsign"]].apply(lambda x: ' - '.join(x.astype(str)), axis=1)
#         #print("DEBUGGING: \n", data.dir_desc)

#         return data.dir_desc.unique().tolist()

#     return dcc.Dropdown(
#                 # options = ["Bus","Tram","Metro"],
#                 id="dir-name",
#                 multi=False,
#                 clearable=False,
#                 className='form-dropdown drop',
#                 placeholder="Select the direction",
#                 persistence="string") #To check ? 






# # def day_render():
# #     return dcc.Dropdown(
# #                 options=[{"label": "weekday", "value" : "1"},{"label":"Saturday", "value":"2"}, {"label": "Sunday", "value":"3"}],
# #                 id="day-name",
# #                 multi=False,
# #                 clearable=False,
# #                 className='form-dropdown drop',
# #                 placeholder="Select the mode",
# #                 persistence="string")

