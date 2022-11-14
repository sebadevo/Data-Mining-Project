from dash import Dash, html
from dash_bootstrap_components.themes import BOOTSTRAP
from dashboard.components.layout import create_layout
from dashboard.enumeration import Type,Day
from database.load_db import load_dataframe
from preprocessing import load_data_and_merge,filter,compute_time_difference,retrieve_info_title
import pandas as pd



def main() -> None: 
    app = Dash(external_stylesheets=[BOOTSTRAP]) #Create an app. the Bootstrap is to change the font
    app.title = "Dashboard"
    data = load_data()
    app.layout = create_layout(app,data) #Creation of layout. 
    app.run()


def load_data(type = Type.Tram,day= Day.Saterday, direction_id =0, stop_id= '5705', short_name = '3', start_date= 20210911):
    data = load_dataframe(day,type.value,direction_id =direction_id, stop_id= stop_id, short_name = short_name, start_date= start_date)
    x,y = compute_time_difference(data)
    data = pd.DataFrame()
    data["x"] = x
    data["y"] = y
    print(data)
    return data

if __name__ == "__main__": 
    main()


