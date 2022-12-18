from dash import Dash, dcc, html, Input, Output, dash_table

from . import ids

import pandas as pd


dataframe = pd.read_csv("src/dashboard/components/scores_line.csv")

# dataframe.to_csv("debug.csv", index=False)
def filter_dataframe(date): 
    data =  dataframe[dataframe.Date==date]
    data.drop(columns="Date", inplace=True, axis=1)
    data.reset_index(drop=True, inplace=True)
    data.sort_values(by=['Score'], inplace=True, ascending=True)
    return data


def render(app: Dash):
    
    
    
    layout = html.Div([
    html.H4('Scores per Lines for a Specific Date'),
    # html.Label('Report type:', style={'font-weight': 'bold'}),
    dash_table.DataTable(id=ids.TABLE,sort_action='native', style_table={
        'overflowY': 'scroll',
        'height': '750px',
        'width' : '30%',
        'marginLeft': 'auto', 
        'marginRight': 'auto'
    })
    ])

    
    @app.callback(
        [Output(component_id=ids.TABLE, component_property='data'), 
        Output(component_id=ids.TABLE, component_property='columns')],
        [Input(ids.DATE_SCORE, 'value')]
    )
    def update_table(input_): 
        # print("checking selected data: ", input_)

        dataframe = filter_dataframe(input_)

        # print("checking dataf: ", dataframe.head())
        columns = [{'name': col, 'id': col} for col in dataframe.columns if col != "Date"]
        data = dataframe.to_dict(orient='records')
        return data, columns
    
    
    # dash_table.DataTable(dataframe.to_dict('records'), [{"name": i, "id": i} for i in dataframe.columns])
    
    return layout

