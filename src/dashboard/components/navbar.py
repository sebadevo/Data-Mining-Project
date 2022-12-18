import dash_bootstrap_components as dbc
from dash import Dash, html ,dcc, Input, Output, State

def render(app : Dash):

    search_bar = html.Ul(
    [   
        html.Li([html.A("Headways", href="#headway")]),
        html.Li([html.A("Statistics", href="#statistics")]),
        html.Li([html.A("Map", href="#about")]),

    ])

    return html.Div([
            html.Div(id="white-nav",children= [
                html.A(
                    [html.Img(src=app.get_asset_url("stib_logo.png"), height="50px")],
                    href="#",
                    style={"textDecoration": "none"},
                ),
            ]),
            html.Div(id="blue-nav",children=[ search_bar]),
            ],
    className="mynav"
    )
    