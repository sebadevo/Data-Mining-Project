from dash import Dash, html, dcc
import plotly.express as px

from dash.dependencies import Output, Input

from . import ids

def render(app: Dash, data) -> html.Div:
    @app.callback(
        Output(ids.BAR_CHART, "figure")
    )
    def update_bar_chart()->html.Div: 
        fig = px.line(data, height=600)
        fig.show()
        return html.Div(children=[dcc.Graph(figure=fig),html.P("Paragrahpe")], id=ids.BAR_CHART)
    return html.Div(id=ids.BAR_CHART)
