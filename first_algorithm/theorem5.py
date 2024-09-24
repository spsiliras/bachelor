from lemma4 import lemma4
from create_set import create_set
import matplotlib.pyplot as plt
import matplotlib.patches as patches

coord_range = [0, 40]
# create_set(# of points of set, coordinates range)
points = create_set(100, coord_range)

points.sort(key=lambda x:x[1])

#rectangle = [x_low, x_high, y_low, y_high]
def plot_points(points, rectangle):
    # Create a new figure and axis
    fig, ax = plt.subplots()

    # Define points to be plotted
    points_x = [p[0] for p in points]
    points_y = [p[1] for p in points]

    # Plot points
    ax.scatter(points_x, points_y, s=5, color='blue', label='Points')

    # Define rectangle parameters (lower-left corner x, y, width, height)
    rect = patches.Rectangle((rectangle[0], rectangle[2]), rectangle[1] - rectangle[0], rectangle[3] - rectangle[2], linewidth=1, edgecolor='red', facecolor='none')

    # Add rectangle to the plot
    ax.add_patch(rect)

    # Set limits for the axes
    ax.set_xlim(coord_range[0] - 5, coord_range[1] + 5)
    ax.set_ylim(coord_range[0] - 5, coord_range[1] + 5)

    # Add labels and title
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_title('Points and Rectangle')

    # Show legend
    ax.legend()

    # Display the plot
    plt.show()

def find_min(min_area_below, min_area_above, min_current_area, best_box_below, best_box_above, current_best):
    if (min_area_below <= min_area_above) and (min_area_below <= min_current_area):
        return min_area_below, best_box_below
    elif (min_area_above <= min_area_below) and (min_area_above <= min_current_area):
        return min_area_above, best_box_above
    else:
        return min_current_area, current_best

def minimize_area(points, num_points):
    # base case scenario
    if len(points) < num_points:
        # then we know that there is not an appropriate box
        return float('inf'), []
    
    # compute median index of sorted points so we can split set
    med_index = len(points) // 2

    # line = c
    line = ((points[med_index][1] - points[med_index - 1][1]) / 2) + points[med_index - 1][1]

    # split set into two sub-sets of roughly equal number of points
    points_below = points[:med_index]
    points_above = points[med_index:]

    min_area_below, best_box_below = minimize_area(points_below, num_points)
    min_area_above, best_box_above = minimize_area(points_above, num_points)

    min_current_area, current_best = lemma4(points, line, num_points)

    return find_min(min_area_below, min_area_above, min_current_area, best_box_below, best_box_above, current_best)

area, box = minimize_area(points, 7)
print(area, box)

plot_points(points, box)