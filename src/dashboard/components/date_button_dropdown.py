from dash import Dash, dcc, html, Input, Output

# from map import display_map_score

from . import map


from . import ids
import pandas as pd

import datetime

dataframe = pd.read_csv("src/dashboard/components/scores_line.csv")

data = sorted(dataframe.Date.unique())

def findDay(date):
    date = str(date)
    year, month, day = int(date[:4]), int(date[4:6]), int(date[6:])
    print("kljdb ", year, month, day)
    weekday = datetime.date(year, month, day)
    return weekday.strftime("%A")


def render(app: Dash):
    layout = html.Div([
        dcc.Dropdown(data,data[0], id=ids.DATE_SCORE),
        html.Div(id=ids.DATE_SCORE_CONTAINER)
    ])

    @app.callback(
        [Output(ids.DATE_SCORE_CONTAINER, 'children'),
        Output(ids.ALL_MAP, 'children')],
        Input(ids.DATE_SCORE, 'value')
    )
    def update_output(value):
        return f'The selected day is {findDay(value)}', map.display_map_score(value)
    return layout
