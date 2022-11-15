from dash import Dash, html ,dcc
from . import dropdown, bar_chart
import plotly.express as px

def create_layout(app: Dash) -> html.Div: 
        return html.Div(
        className= "app-div", 
        children=[
            html.H1("The title of the plot"),
            html.Div(className="dropdown-menu",children=[
                dropdown.mode_render(),
                dropdown.line_name_render(app),
                dropdown.stop_id_render(app), 
                # dcc.Dropdown(id="stop-name",
                #     options=[{'label':"po",'value':'yes'},{'label':"za",'value':'no'}],
                #     multi=False,
                #     disabled=True,
                #     clearable=False,
                #     className='form-dropdown drop',
                #     persistence="string"),
                dcc.Dropdown(id="direction",
                    options=[{'label':"po",'value':'yes'},{'label':"za",'value':'no'}],
                    multi=False,
                    disabled=True,
                    clearable=False,
                    className='form-dropdown drop',
                    persistence="string"),
                dcc.Dropdown(id="day",
                    options=[{'label':"po",'value':'yes'},{'label':"za",'value':'no'}],
                    multi=False,
                    clearable=False,
                    disabled=True,
                    className='form-dropdown drop',
                    persistence="string"),
                dcc.Dropdown(id="start-date",
                    options=[{'label':"po",'value':'yes'},{'label':"za",'value':'no'}],
                    multi=False,
                    disabled=True,
                    clearable=False,
                    className='form-dropdown drop',
                    persistence="string"),
                    
                ]),
            #dcc.Graph(id="graph1",figure=fig),
            bar_chart.render(app),
        ]
    )
