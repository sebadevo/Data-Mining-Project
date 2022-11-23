import geopandas
import matplotlib.pyplot as plt
import numpy as np


if __name__ == "__main__":
    #df = geopandas.read_file(geopandas.datasets.get_path('naturalearth'))
    fig, ax = plt.subplots(figsize = (20,16)) 
    df = geopandas.read_file("data/shapefiles23Sept/2109_STIB_MIVB_Network/ACTU_LINES.shp")
    print(df.head())
    df.plot(figsize=(10, 10), alpha=0.5, edgecolor='k',ax=ax)
    df = geopandas.read_file("data/shapefiles23Sept/2109_STIB_MIVB_Network/ACTU_STOPS.shp")
    print(df.head())
    print(df['mode'].unique())


    df = df[df["mode"] == "M"]
    """df.explore(
     column="descr_fr", # make choropleth based on "BoroName" column
     tooltip="BoroName", # show "BoroName" value in tooltip (on hover)
     popup=True, # show all values in popup (on click)
     tiles="CartoDB positron", # use "CartoDB positron" tiles
     cmap="Set1", # use "Set1" matplotlib colormap
     style_kwds=dict(color="black"), # use black outline
     ax = ax
    )"""
    df.plot(figsize=(10, 10), alpha=0.5, edgecolor='k',ax=ax)

    plt.show()
