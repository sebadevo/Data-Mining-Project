import geopandas
import matplotlib.pyplot as plt
import numpy as np
import folium


#https://geopandas.org/en/stable/docs/user_guide/interactive_mapping.html
if __name__ == "__main__":
    #df = geopandas.read_file(geopandas.datasets.get_path('naturalearth'))
    fig, ax = plt.subplots(figsize = (20,16)) 
    df = geopandas.read_file("data/shapefiles23Sept/2109_STIB_MIVB_Network/ACTU_LINES.shp")
    print(df.head())
    #df.plot(figsize=(10, 10), alpha=0.5, edgecolor='k',ax=ax)
    df = geopandas.read_file("data/shapefiles23Sept/2109_STIB_MIVB_Network/ACTU_STOPS.shp")
    print(df.head())
    print(df['mode'].unique())


    df = df[df["mode"] == "M"]
    m = df.explore(
     column="descr_fr", # make choropleth based on "BoroName" column
     tooltip="descr_fr", # show "BoroName" value in tooltip (on hover)
     style_kwds=dict(labels=False), # use black outline
     name = "stops",
     color="red",
    )
    folium.TileLayer('Stamen Toner', control=True).add_to(m)  # use folium to add alternative tiles
    folium.LayerControl().add_to(m)  # use folium to add layer control
    #df.plot(figsize=(10, 10), alpha=0.5, edgecolor='k',ax=ax)

    plt.show()
