import geopandas
import matplotlib.pyplot as plt



if __name__ == "__main__":
    #df = geopandas.read_file(geopandas.datasets.get_path('naturalearth'))
    df = geopandas.read_file("data/shapefiles23Sept/2109_STIB_MIVB_Network/ACTU_LINES.shp")
    ax = df.plot(figsize=(10, 10), alpha=0.5, edgecolor='k')
    plt.show()
    df = geopandas.read_file("data/shapefiles23Sept/2109_STIB_MIVB_Network/ACTU_STOPS.shp")
    ax = df.plot(figsize=(10, 10), alpha=0.5, edgecolor='k')
    plt.show()
