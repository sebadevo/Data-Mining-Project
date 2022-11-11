from dash import Dash, html
from dash_bootstrap_components.themes import BOOTSTRAP
from components.layout import create_layout

def main() -> None: 
    app = Dash(external_stylesheets=[BOOTSTRAP]) #Create an app. the Bootstrap is to change the font
    app.title = "Dashboard"
    app.layout = create_layout(app) #Creation of layout. 
    app.run()

if __name__ == "__main__": 
    main()