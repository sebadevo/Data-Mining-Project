from dash import Dash, html ,dcc
from . import dropdown, bar_chart,navbar, all_line,all_stop,direction, real_data_chart, map, metric_plot, statistics, stop_score_chart,map
import plotly.express as px
from dash.dependencies import Output, Input,MATCH,State
from . import ids

import dash

def create_layout(app: Dash) -> html.Div: 
    return html.Div(
        className= "app-div", 
        children=[
            dcc.Store(id=ids.SELECTED_LINE),
            navbar.render(app),
            all_line.render(app),
            direction.render(app),
            create_dropdown_menu(app),
            html.H1("Headways",id="headway"),   
            bar_chart.render(app),
            real_data_chart.render(app),
            html.H1("Statistics",id="statistics"),
            statistics.render(app),
            html.Div(id= ids.DIV_MAP),
            html.H1("Map",id="about"),
            map.display_all_map()
        ]
    )

def create_dropdown_menu(app):

    return  html.Div(className="dropdown-menu",children=[
                dropdown.stop_id_render(app), 
                dropdown.day_render(app),
                dropdown.date_render(app),
                dropdown.real_date_render(app),
                ], 
     )

    #  style = {"align-items": "center", "justify-content": "center"}