from dash import Dash, html ,dcc
import dash_bootstrap_components as dbc
import dash
from dash.dependencies import Output, Input,ALL


metro = [1,2,5,6]
tram = [3,4,7,8,9,19,25,39,44,51,55,62,81,82,92,93,97]
bus = [12,13,14,"T19",20,21,27,28,29,33,34,36,37,38,
    41,42,43,45,46,47,48,49,50,52,53,54,56,57,58,59,60,61,63,
    64,65,66,69,70,71,72,73,74,75,76,77,78,79,80,"T81","T82",83,86,87,88,89,90,"T92",95]
noctis = ["04","05","06","08","09","10","11","12","13","16","18"]

all_line = metro + tram + bus
def render(app: Dash) -> html.Div: 

    @app.callback(Output('lineis', 'hidden'),
        Output('box-all-lines',"hidden"),
        Output('lineis',"children"),
        Output('actual_line',"data"),
        [Input("button_{}".format(_), "n_clicks") for _ in all_line],
        [Input("noctis_{}".format(_), "n_clicks") for _ in noctis],
        Input("button_selected","n_clicks"),
        prevent_initial_call=True)
    def display_click_hide_lines(*clicks):
        if dash.callback_context.triggered_id == "button_selected":
            return html.Div(),False,[html.Button("1", id="chosen_line",className="line line--1"),html.Button("X", className="line line--X", id="button_selected")],0
        msg=[p['prop_id'] for p in dash.callback_context.triggered][0]
        print("balbal ", msg)
        msg = msg.split("_")[1].split(".")[0]
        if "noctis" in dash.callback_context.triggered_id:
            return False, True, [generate_noctis_selected(msg), html.Button("X", className="line line--X", id="button_selected")], f'n{str(msg)}'
        return False, True, [generate_line_selected(msg),  html.Button("X", className="line line--X", id="button_selected")],msg

    return html.Div(
    className= "box all-lines",
    children=[html.Div([
            html.Button("1", id="chosen_line",className="line line--1"),
            html.Button("X", className="line line--X", id="button_selected"),]
            ,id="lineis",style={"hidden":"True"}),
            html.Div(className="container",id="box-all-lines",
            children = [
            html.Div(className="col--12",children=[
                html.Div(className="all-lines__item", children=[
                    html.H2(children=[html.Span(className="mode",children=[html.Span("M",className="mode__inner")]),"Metro"]),
                    html.Div(children = [generate_line(i) for i in metro]),
                ]),
                html.Div(className="all-lines__item", children=[
                    html.H2(children=[html.Span(className="mode",children=[html.Span("T",className="mode__inner")]),"Tram"]),
                    html.Div(children = [generate_line(i) for i in tram]),
                ]),
                html.Div(className="all-lines__item", children=[
                    html.H2(children=[html.Span(className="mode",children=[html.Span("B",className="mode__inner")]),"Bus"]),
                    html.Div(children = [generate_line(i) for i in bus]),
                ]),
                html.Div(className="all-lines__item", children=[
                    html.H2(children=[html.Span(className="mode",children=[html.Span("N",className="mode__inner")]),"Noctis"]),
                    html.Div(children = [generate_noctis(i) for i in noctis]),
                ])
            ]),
        ]),

    ])



def generate_line_selected(i):
    return html.Button(f"{i}", className=f"line line--{i}", id="chosen_line")

def generate_line(i):
    return html.Button(f"{i}",className=f"line line--{i}",id=f"button_{i}")

def generate_noctis_selected(i):
    return html.Button([html.Span("n"),f"{i}"],className=f"line line--N{i}",id="chosen_line")
def generate_noctis(i):
    return html.Button([html.Span("n"),f"{i}"],className=f"line line--N{i}",id=f"noctis_{i}")



