from dash import Dash, html
from dash_bootstrap_components.themes import BOOTSTRAP
from dashboard.components.layout import create_layout
from dashboard.components.all_line import create_all_line
from dashboard.enumeration import Type,Day
from database.load_db import load_dataframe
from preprocessing import load_data_and_merge,filter,compute_time_difference,retrieve_info_title
import pandas as pd
import plotly.express as px



def main() -> None: 
    app = Dash(__name__ ) #Create an app. the Bootstrap is to change the font
    app.title = "Dashboard"
    app.layout = create_layout(app) #Creation of layout. 
    # app.layout = create_all_line(app) #Creation of layout.
    app.run()



if __name__ == "__main__": 
    main()


