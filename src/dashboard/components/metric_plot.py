import dash_bootstrap_components as dbc
from dash import Dash, html ,dcc, Input, Output, State
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px


def render(app : Dash):
    stat = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]
    x = [5,6,7,8,9,10,11,12,13,14,15]
    middle = []
    width = []
    for i in range(len(x)-1):
        middle.append((x[i+1] + x[i])/2)
        width.append(x[i+1] - x[i])

    fig = go.Figure(data=[go.Bar(
        x=middle,
        y=stat,
        width=width,
          marker=dict(
            color=stat,
            colorscale='RdYlGn',
            showscale=True
    ))])
    fig.update_yaxes(title_text="Quality")
    fig.update_xaxes(title_text="Time") 
    return html.Div([
            html.A("The quality depending on the time interval of the bus stop"),
            dcc.Graph(figure=fig)
        ],
        className="metric-plot"
    )
    