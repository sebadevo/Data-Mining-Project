from dash import Dash, html ,dcc
from . import dropdown, bar_chart,navbar, all_line,all_stop,direction
import plotly.express as px
from dash.dependencies import Output, Input,MATCH,State

import dash

def create_layout(app: Dash) -> html.Div: 
    return html.Div(
        className= "app-div", 
        children=[
            dcc.Store(id='actual_line'),
            navbar.render(app),
            all_line.render(app),
            direction.render(app),
            all_stop.render(app),
            create_dropdown_menu(app),
            html.H1("Headways",id="headway"),
            bar_chart.render(app),
            html.H1("Statistics",id="statistics"),
            html.H1("About",id="about"),])

def create_dropdown_menu(app):
    return  html.Div(className="dropdown-menu",children=[
                dropdown.mode_render(),
                dropdown.line_name_render(app),
                dropdown.stop_id_render(app), 
                dropdown.direction_id_render(app),
                dropdown.day_render(app),
                dcc.Dropdown(id="start-date",
                    options=[{'label':"po",'value':'yes'},{'label':"za",'value':'no'}],
                    multi=False,
                    disabled=True,
                    clearable=False,
                    className='form-dropdown drop',
                    persistence="string"),
                ])