from dash import Dash, html
from dash_bootstrap_components.themes import BOOTSTRAP
from dashboard.components.layout import create_layout
from dashboard.enumeration import Type,Day
from database.load_db import load_dataframe
from preprocessing import load_data_and_merge,filter,compute_time_difference,retrieve_info_title
import pandas as pd
import plotly.express as px



def main() -> None: 
    app = Dash(__name__,use_pages=True ,external_stylesheets=[BOOTSTRAP]) #Create an app. the Bootstrap is to change the font
    app.title = "Dashboard"
    app.layout = create_layout(app) #Creation of layout. 
    app.run()



if __name__ == "__main__": 
    main()


