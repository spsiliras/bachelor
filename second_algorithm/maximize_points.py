from create_set import create_set
from scipy.spatial import KDTree
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# dimensions of the block of points
coord_range = [0, 40]
# the number of points to be created
user_num_points = 40
# the specific area of the box, given by the user
user_area = 20


# create_set(# of points of set, coordinates range)
points = create_set(user_num_points, coord_range)

#points = [[1, 7], [4, 4], [5, 2], [7, 1]]

# sort points by its y-coordinate
points.sort(key=lambda x:x[1])

# store points in a kd-tree so its more efficient to query if a point is inside box
tree = KDTree(points)

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

    # Display the plot
    plt.show()

# return the number of points inside rectangle and also the points for the best solution
def count_points_inside(x_low, x_high, y_low, y_high):
    points_in_box = tree.query_ball_point([x_low, y_low], r=max(x_high - x_low, y_high - y_low))

    filtered_points_indices = [p for p in points_in_box if x_low <= points[p][0] <= x_high and y_low <= points[p][1] <= y_high]                          
    
    # find the points inside the box
    #points_inside = [points[p] for p in filtered_points_indices]

    return len(filtered_points_indices)

# returns the maximum number of points inside a box 
# considering the curremt line and the four boxes explained in paper
def current_max_inside(line, points, area):
    count = 0
    best_box = []

    for p in points:
        # point above line l
        if p[1] > line:
            # we know that area = (y_high - y_low)*(x_high - x_low), so we compute the needed values
            x_low = p[0]
            x_high = (area + (p[0] * (p[1] - line))) / (p[1] - line)
            y_low = line
            y_high = p[1]

            count_right = count_points_inside(x_low, x_high, y_low, y_high)
            if count_right > count:
                count = count_right
                best_box = [x_low, x_high, y_low, y_high].copy()

            x_low = ((p[0] * (p[1] - line)) - area) / (p[1] - line)
            x_high = p[0]

            count_left = count_points_inside(x_low, x_high, y_low, y_high)
            if count_left > count:
                count = count_left
                best_box = [x_low, x_high, y_low, y_high].copy()

        if p[1] < line:
            x_low = p[0]
            x_high = (area + (p[0] * (line - p[1]))) / (line - p[1])
            y_low = p[1]
            y_high = line

            count_right = count_points_inside(x_low, x_high, y_low, y_high)
            if count_right > count:
                count = count_right
                best_box = [x_low, x_high, y_low, y_high].copy()

            x_low = ((p[0] * (line - p[1])) - area) / (line - p[1])
            x_high = p[0]

            count_left = count_points_inside(x_low, x_high, y_low, y_high)
            if count_left > count:
                count = count_left
                best_box = [x_low, x_high, y_low, y_high].copy()

    return count, best_box

def find_max(max_below, max_above, max_current, box_below, box_above, box_current):
    if (max_below >= max_above) and (max_below >= max_current):
        return max_below, box_below
    elif (max_above >= max_below) and (max_above >= max_current):
        return max_above, box_above
    else:
        return max_current, box_current

# returns the max number of points inside a box with area a
def max_points_in_box(points, area, line):
    # base case of recursion
    if len(points) <= 2:
        
        return current_max_inside(line, points, area)
    
    med_index = len(points) // 2

    # line = c
    line = (points[med_index][1] + points[med_index - 1][1]) / 2

    # split set into two sub-sets of roughly equal number of points
    points_below = points[:med_index]
    points_above = points[med_index:]

    max_below, box_below = max_points_in_box(points_below, area, line)
    max_above, box_above = max_points_in_box(points_above, area, line)

    max_current, box_current = current_max_inside(line, points, area)

    return find_max(max_below, max_above, max_current, box_below, box_above, box_current)

med = len(points) // 2

# line = c
init_line = (points[med][1] + points[med - 1][1]) / 2

solution = max_points_in_box(points, user_area, init_line)

print(solution)
plot_points(points, solution[1])

