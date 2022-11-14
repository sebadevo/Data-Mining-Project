from dash import Dash, html 
from . import mode_dropdown, bar_chart


def create_layout(app: Dash, data) -> html.Div: 
    return html.Div(
        className= "app-div", 
        children=[
        bar_chart.render(app,data),
        html.H1("The title of the plot")
        ]
    )