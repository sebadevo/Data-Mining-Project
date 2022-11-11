import matplotlib.pyplot as plt

def plot_schedulde_headways(x,y, line, line_name, trip_headsign, stop_name,color = None):

    title = f"Scheduled headways on line {line} - {line_name} to {trip_headsign} at the stop {stop_name} on a saturday"

    plt.figure(figsize=[15,10])
    if color is None:
        plt.plot(x, y)
    else:
        plt.scatter(x, y,color)
    plt.title(title)
    plt.show()


