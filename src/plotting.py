import matplotlib.pyplot as plt

def plot_schedulde_headways(x,y, line, line_name, trip_headsign, intervals, stop_name,type=type,color = None):

    title = f"Scheduled headways of the {type.name} on line {line} - {line_name} to {trip_headsign} at the stop {stop_name} on a saturday"

    plt.figure(figsize=[15,10])
    if color is None:
        plt.plot(x, y)
    else:
        plt.scatter(x, y,color)
    for line in intervals:
        plt.axvline(x = line, color = 'r', label = 'axvline - full height')
    plt.title(title)
    plt.show()


