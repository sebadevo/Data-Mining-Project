from dash import Dash
from dashboard.components.layout import create_layout



def main() -> None: 
    app = Dash(__name__ ) #Create an app. the Bootstrap is to change the font
    app.title = "Dashboard"
    app.layout = create_layout(app) #Creation of layout. 
    # app.layout = create_all_line(app) #Creation of layout.
    app.run()



if __name__ == "__main__": 
    main()


