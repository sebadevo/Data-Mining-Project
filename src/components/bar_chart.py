from dash import Dash, html, dcc
import plotly.express as px

from dash.dependencies import Output, Input

from . import ids

#ONLY FOR ILLUSTRAION: 

MEDAL_DATA = px.data.medals_long()

def render(app: Dash) -> html.Div:
    @app.callback(
        Output(ids.BAR_CHART, "children"),
        Input(ids.MODE_DROPDOWN, "value")
    )
    def update_bar_chart(modes: list[str])->html.Div: 
        filtered_data = MEDAL_DATA.query("nation in @modes") #Use the arg. of the fct. to filter the dataframe
        fig = px.bar(filtered_data, x="medal", y="count", color="nation", text="nation") #mode instead of nation
        if filtered_data.shape[0] ==0: 
            return html.Div("No data selected.")
        return html.Div(dcc.Graph(figure=fig), id=ids.BAR_CHART)
    return html.Div(id=ids.BAR_CHART)
