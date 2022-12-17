from dash import Dash, html, dcc,ctx
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



def which_date(value): 
    return value.split(" - ")

def which_day(value): 
    Weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    return "Weekday" if value in Weekdays else value

def plot_weight( day, precision=60):

    if day in Weights:
        weights = Weights[day]
    else: 
        print(f"the day received is not in the available days : {list(Weights.keys())}. day received =", day)
        return 0
    
    x = [i/precision for i in range(24*precision) ]
    weights = [weights[floor(i/precision)] for i in range(24*precision)]
    fig = go.Figure(data=[go.Bar(
        x=x,
        y=weights,
    )])
    fig.update_yaxes(title_text="Weights")
    fig.update_xaxes(title_text="Time",
                    range=[0,27]) 
    fig.update_layout(title={
                    'text': "<b>Weights for personnalised metric<b>",
                    'y':0.87,
                    'x':0.5,
                    'xanchor': 'center',
                    'yanchor': 'top'},
                    font=dict(size=18,))
    return fig
    




def plot_interval_scores(qualities, intervals, day):
    stat = qualities
    stat = [round(i*100,2) for i in qualities]
    x = intervals
    middle = []
    width = []
    for i in range(len(x)-1):
        middle.append((x[i+1] + x[i])/2)
        width.append((x[i+1] - x[i]))

    fig = go.Figure(data=[go.Bar(
        x=middle,
        y=stat,
        text = stat,
        textposition='outside', 
        cliponaxis = False,
        textfont = dict(
            size= 20, color='black',
        ), 
        # insidetextanchor = "middle"
        width=width,
        marker=dict(
            color=stat,
            colorscale='RdYlGn',
            showscale=True,
            cmin=0,
            cmax=100,
    ))])
    fig.update_yaxes(title_text="Quality")
    fig.update_xaxes(title_text="Time", 
                     range=[0,26.4])  # sets the range of xaxis) 
    fig.update_layout(title={
                    'text': "<b>The quality depending on the time interval of the stop<b>",
                    'y':0.89,
                    'x':0.5,
                    'xanchor': 'center',
                    'yanchor': 'top'},
                    font=dict(size=18,))
    return fig


def render(app: Dash) -> html.Div:
    @app.callback(
            Output(ids.INTERVAL_SCORE_CHART, "children"),
            State(ids.SELECTED_LINE,'data'),
            State(ids.STOP, 'value'),
            State(ids.DATE, 'value'),
            Input(ids.REAL_DATE, 'value'),
            Input("reset","n_clicks"),
            prevent_initial_call=True
            )

    def update_bar_chart(line_name, stop_name,date, real_date_name ) -> html.Div:  
        if ctx.triggered_id == "reset":
            return html.Div()
        stop_name = stop_name.split(' - ')[0]
        real_date_name, day = real_date_name.split(' - ')
        day = which_day(day)
        if (which_type(line_name) == 1): #For metros
            query = ( 
                "select rd.time, rd.distanceFromPoint"
                " from real_data rd" 
                " where rd.lineID = %s and rd.pointID = %s and rd.date = %s"
                )
        elif (which_type(line_name) == 0): #For trams
            query = ( 
                "select rd.time, rd.distanceFromPoint"
                " from real_data rd" 
                " where rd.lineID = %s and rd.pointID = %s and rd.date = %s"
                )
        elif (which_type(line_name) == 3): #for buses
            query = ( 
                "select rd.time, rd.distanceFromPoint"
                " from real_data rd" 
                " where rd.lineID = %s and rd.pointID = %s and rd.date = %s"
                )
        else: 
            return html.Div(html.H4("This feature has not been implemented yet, would you kindly select a line from a metro and go on as if nothing happened ? \n"
            "from the developpers team."))
        connection = get_connection()
        start_time = process_time()
        real_data = pd.read_sql(query, params=[line_name, stop_name, real_date_name], con= connection)
        query = (
            "select st.arrival_time, c.monday, c.saturday, c.sunday"
            " from trips tr" 
            " inner join routes ro on tr.route_id = ro.routes_id"
            " inner join stop_times st on st.trip_id = tr.trip_id"
            " inner join stops s on s.stop_id = st.stop_id"
            " inner join calendar c on c.service_id = tr.service_id"
            " where ro.route_type = %s and ro.routes_short_name = %s and st.stop_id = %s and c.start_date = %s and c.end_date = %s"
            )
        connection = get_connection()
        data = pd.read_sql(query, params=[which_type(line_name), line_name, stop_name, int(which_date(date)[0]), int(which_date(date)[1])], con= connection)

        if( len(real_data) < 5):
            return html.Div(html.H4(f"There is not enough data to plot a graph (number of lines in the data is: {len(real_data)})"))
        
        
        
        time_real = map_to_sec(real_data.time.tolist())
        time_th = map_to_sec(data.arrival_time.tolist())
        distance_real = real_data.distanceFromPoint.tolist()

        if (which_type(line_name) == 1): #For metros
            time_real = remove_duplicates_metro(time_real, distance_real)
        elif (which_type(line_name) == 0): #For trams
            time_real = remove_duplicates_tram(time_real, distance_real)
        elif (which_type(line_name) == 3): #for buses
            time_real = remove_duplicates_bus(time_real, distance_real)
        else:
            print("there was an error")
            time_real = remove_duplicates(time_real)


        x,y = get_headway(time_th)
        intervals = get_interval(x,y)
        categories = get_categories(x, y, intervals)

        if (len(time_th) < len(time_real)): 
            scheduled_times, real_times = find_match_V2(time_th, time_real)
        else: 
            real_times, scheduled_times = find_match_V2(time_real, time_th)


        real_headways_x,real_headways_y = get_headway(real_times)
        scheduled_headways_x,scheduled_headways_y = get_headway(scheduled_times)
        qualities = interval_score(scheduled_times, real_times, scheduled_headways_x, real_headways_x, scheduled_headways_y, real_headways_y, intervals, categories)
        fig_weights = plot_weight(day)
        fig_interval_scores = plot_interval_scores(qualities, intervals, day)

        return html.Div([html.Div([
            dcc.Graph(figure=fig_interval_scores), 
            dcc.Graph(figure=fig_weights),
            html.H1(f"The quality of the stop is: {round(stop_score(qualities, intervals, day)*100, 3)}%", style={'color': 'black', 'fontSize': 28})],
            
    )], className="metric-plot", id=ids.INTERVAL_SCORE_CHART)
    return html.Div(id=ids.INTERVAL_SCORE_CHART)