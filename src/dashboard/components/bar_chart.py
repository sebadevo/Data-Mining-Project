from dash import Dash, html, dcc
import plotly.express as px
from dashboard.enumeration import Type,Day
from utils import *
from dash.dependencies import Output, Input
from . import ids

from database.load_db import load_dataframe
from preprocessing import load_data_and_merge,filter,compute_time_difference,retrieve_info_title
import pandas as pd


def render(app: Dash) -> html.Div:
    @app.callback(
            Output(ids.BAR_CHART, "children"),
            [Input('mode','value')])
    def update_bar_chart(mode) -> html.Div:  
        def load_data(type = Type.Tram,day= Day.Saterday, direction_id =0, stop_id= '5705', short_name = '3', start_date= 20210911):
            data = load_dataframe(day,type.value,direction_id =direction_id, stop_id= stop_id, short_name = short_name, start_date= start_date)
            x,y = compute_time_difference(data)
            lines = get_interval(x, y)
            data = pd.DataFrame()
            data["x"] = x
            data["y"] = y
            print(data)
            return data, lines

        if mode not in ["0","1","3"] :
            return html.Div("chey",id=ids.BAR_CHART)
        data, lines = load_data(type = Type.Tram,day= Day.Saterday, direction_id =0, stop_id= '5705', short_name = '3', start_date= 20210911)
        fig = px.line(data,x="x",y="y")
        for line in lines:
            fig.add_vline(x = line, line_color = 'red')


        return html.Div(dcc.Graph(figure=fig), id=ids.BAR_CHART)

    return html.Div(id=ids.BAR_CHART)


