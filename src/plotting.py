import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from statistics import mean

def plot_schedulde_headways(x,y, line, line_name, trip_headsign, intervals, stop_name,type=type,color = None):

    title = f"Scheduled headways of the {type.name} on line {line} - {line_name} to {trip_headsign} at the stop {stop_name} on a saturday"

    plt.figure(figsize=[20,10])
    if color is None:
        plt.bar(x, y, width=0.05)
    else:
        plt.scatter(x, y,color)

    for i in range(len(intervals)-1):
        beg = x.index(intervals[i])
        end = x.index(intervals[i+1])
        width = 0
        if i != len(intervals)-2:
            end -= 1

        average = mean(y[beg:end])
        color = 'red' if average > 12 else 'green'
        width += x[end]-x[beg] + 0.15
        if color == "red":
            plt.gca().add_patch(Rectangle((x[beg]-0.075,0), width, max(y[beg:end])+1.5,
                        edgecolor=color,
                        facecolor='none',
                        lw=2))
        else:
            plt.gca().add_patch(Rectangle((x[beg]-0.075,0), width, mean(y[beg:end])+3,
                        edgecolor=color,
                        facecolor='none',
                        lw=2))
    # for line in intervals:
    #     plt.axvline(x = line, color = 'r', label = 'axvline - full height')
    plt.title(title)
    plt.show()


