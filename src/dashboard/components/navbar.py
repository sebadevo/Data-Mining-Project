import dash_bootstrap_components as dbc
from dash import Dash, html ,dcc, Input, Output, State
import dash

def render(app : Dash):

    search_bar = dbc.Nav(
    [
        dbc.NavLink("Headways", href="#",class_name="link"),
        dbc.NavLink("Statistics", href="#",class_name="link"),
        dbc.NavLink("About", href="#",class_name="link"),
    ],
    className="mynavbar",
)
    # add callback for toggling the collapse on small screens
    @app.callback(
            Output("navbar-collapse", "is_open"),
            [Input("navbar-toggler", "n_clicks")],
            [State("navbar-collapse", "is_open")],
        )
    def toggle_navbar_collapse(n, is_open):
        return not is_open if n else is_open

    return dbc.Navbar(
    dbc.Container(
        [
            html.A(
                dbc.Row(
                    [
                        dbc.Col(html.Img(src=app.get_asset_url("stib_logo_grey.png"), height="50px"))
                    ],
                    align="center",
                    className="g-0",
                ),
                href="#",
                style={"textDecoration": "none"},
            ),
            dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
            dbc.Collapse(
                search_bar,
                id="navbar-collapse",
                is_open=False,
                navbar=True,
            ),
        ]
    ),
    color="dark",
    dark=True,
    id="mynav"
    )