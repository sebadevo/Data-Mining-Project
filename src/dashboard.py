import pandas as pd
import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# from database.load_db import load_dataframe


app = dash.Dash(__name__)

#---------------------------------------------------------------

df=pd.read_csv("./data/FinalDF.csv")
# df = df.groupby(['trip_id','stop_id'], as_index=False)
# print (df[:5])

#---------------------------------------------------------------
app.layout = html.Div([

    html.Div([
        dcc.Graph(id='line_graph')
    ],className='graph'),

    html.Div([

        html.Br(),
        html.Label(['Choose the parameters'],style={'font-weight': 'bold', "text-align": "center"}),
        dcc.Dropdown(id='direction',
            options=[{'label':x, 'value':x} for x in df.direction_id.unique()],
            value='1', #Value by default
            multi=False,
            # disabled=False,
            clearable=False,
            searchable=True,
            placeholder='Choose Direction...',
            className='form-dropdown', #For the style
            # style={'width':"90%"},
            persistence='number',
            persistence_type='session'),

        dcc.Dropdown(id='day_weekend',
            options=[{'label':x, 'value':x} for x in df.saturday.unique()],
            value='1',
            multi=False,
            clearable=False,
            searchable=True,
            placeholder='Choose Saturday...', #choose 1!
            persistence='number',
            persistence_type='session'),

        dcc.Dropdown(id='stop',
            options=[{'label':x, 'value':x} for x in df.stop_id.unique()],
            value='5705',
            multi=False,
            clearable=False,
            searchable=True,
            placeholder='Choose stop_id ...',
            persistence='string',
            persistence_type='session'),

        dcc.Dropdown(id='route_short_name',
            options=[{'label':x, 'value':x} for x in df.route_short_name.unique()],
            value='3',
            multi=False,
            clearable=False,
            searchable=True,
            placeholder='Choose route short name...',
            persistence='string',
            persistence_type='session'),
        
        dcc.Dropdown(id='date',
            options=[{'label':x, 'value':x} for x in df.start_date.unique()],
            value='20210911',
            multi=False,
            clearable=False,
            searchable=True,
            placeholder='Choose start date...',
            persistence='number',
            persistence_type='session'),

    ],className='five columns'),

        

])

def time_to_sec(time:str):
    time = time.split(":")
    hours, minutes, seconds = int(time[0]), int(time[1]), int(time[2])
    return hours*60*60+minutes*60+seconds

#---------------------------------------------------------------

@app.callback(
    Output('line_graph','figure'),
    [Input('direction','value'),
     Input('day_weekend','value'),
     Input('stop','value'),
     Input('route_short_name', 'value'), 
     Input('date', 'value')]
)



def build_graph(direc, day, stop, route_name, date):
    time, headway = [], []

    dff=df[(df['direction_id']==direc) &
           (df['saturday']==day) &
           (df['stop_id']==stop) &
           (df['route_short_name'] == route_name) &
           (df['start_date'] == date)]
    
    arrival_times = df['arrival_time']#.tolist()
    arrival_times_minutes = map(time_to_sec, arrival_times)
    arrival_times_minutes = sorted(arrival_times_minutes)

    for i in range(len(arrival_times_minutes)-1):
        time.append(round((arrival_times_minutes[i+1]-arrival_times_minutes[i])/60, 2))
        headway.append(round(arrival_times_minutes[i]/3600, 2))

    fig = px.line(dff, x=time, y=headway, height=600)
    fig.update_layout(yaxis={'title':'HEADWAY'}, xaxis={'title':'TIME'},
                      title={'text':'Line Plot',
                      'font':{'size':28},'x':0.5,'xanchor':'center'})
    return fig

#---------------------------------------------------------------

if __name__ == '__main__':
    app.run_server(debug=False)