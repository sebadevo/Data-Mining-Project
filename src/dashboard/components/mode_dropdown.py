from dash import Dash, html, dcc
from . import ids
from dash.dependencies import Input, Output



def render(app:Dash) -> html.Div: 
    # all_modes = ["Metro", "Tram", "Bus"]
    all_modes=["China", "Canada", "South Korea"]
    # Define a callback so that the button "Select all" does smth. 
    @app.callback(
        Output(ids.MODE_DROPDOWN, "value"),
        Input(ids.SELECT_ALL_MODES_BUTTON, "n_clicks")
    )

    def select_all_modes(_: int) -> list[str]: #Just want to make sure we click at least once on the button
        return all_modes
        

    return html.Div(
        children=[
            html.H6("Mode"), 
            dcc.Dropdown(
                id=ids.MODE_DROPDOWN,
                options=[{"label": mode, "value": mode} for mode in all_modes],
                value=all_modes,
                multi=True,
            ),
            html.Button(
                className="dropdown-button", 
                children=["Select All"],
                id = ids.SELECT_ALL_MODES_BUTTON,
            )
        ]
    )