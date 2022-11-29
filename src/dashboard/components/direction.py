from dash import Dash, html
from dash.dependencies import Output, Input
import dash

def render(app : Dash):
    @app.callback(
        Output('dir-1',"className"),
        Output('dir-2', "className"),
        Output('dir-1',"disabled"),
        Output('dir-2', "disabled"),
        [Input('dir-1','n_clicks'),
        Input('dir-2','n_clicks')]
    )
    def enable_dropdown_stop(*clicks): 
        if "1" in dash.callback_context.triggered_id:
            return  "direction direction--2 v navigable", "direction direction--2 f direction--inactive navigable", True,False
        if "2" in dash.callback_context.triggered_id:
            return  "direction direction--2 v direction--inactive navigable", "direction direction--2 f navigable", False,True
        return "direction direction--2 v direction--inactive navigable", "direction direction--2 f navigable", False,True
    @app.callback(
    Output('directions-container', 'children'),
    Input('actual_line', 'data'),
    )
    def change_button(value):
        print("debug ", value)
        return[html.Div([
            html.Button([f"{value} Simonis"],className="direction direction--2 v direction--inactive navigable" ,disabled=False,id="dir-1",tabIndex="0"),
        ],className="direction-container"),
        html.Div([
            html.Button([f"{value} Elisabeth"],className="direction direction--2 f navigable" ,id="dir-2",disabled=True,tabIndex="0"),
        ],className="direction-container")]

    return html.Div([
        html.Div([
            html.Button(["Simonis"],className="direction direction--2 v direction--inactive navigable" ,disabled=False,id="dir-1",tabIndex="0"),
        ],className="direction-container"),
        html.Div([
            html.Button(["Elisabeth"],className="direction direction--2 f navigable" ,id="dir-2",disabled=True,tabIndex="0"),
        ],className="direction-container"),
    ],  
        className="directions-container",
        id="directions-container"
    )
        
def generate_left_button():
    pass


def generate_right_button():
    pass