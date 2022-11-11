from dash import Dash, html 
from . import mode_dropdown, bar_chart


def create_layout(app: Dash) -> html.Div: 
    return html.Div(
        className= "app-div", 
        children=[html.H1(app.title),
        html.Hr(), 
        html.Div(
            className="dropdown-container", 
            children=[
                mode_dropdown.render(app)
            ]
        ), 
        bar_chart.render(app),
        ]
    )