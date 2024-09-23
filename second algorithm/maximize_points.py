from create_set import create_set
from scipy.spatial import KDTree
import matplotlib.pyplot as plt
import numpy as np

# use this function to create the data set of 2D points
points = create_set()

# store points in a kd-tree so its more efficient to query if a point is inside box
tree = KDTree(points)

# sort points by its y-coordinate
points.sort(key=lambda x:x[1])

# return the number of points inside rectangle and also the points for the best solution
def count_points_inside(x_low, x_high, y_low, y_high):
    points_in_box = tree.query_ball_point([x_low, y_low], r=max(x_high - x_low, y_high - y_low))

    filtered_points_indices = [p for p in points_in_box if x_low <= points[p][0] <= x_high and y_low <= points[p][1] <= y_high]                          
    
    # find the points inside the box
    #print([points[p] for p in filtered_points_indices])

    return len(filtered_points_indices)

'''xa = []
ya = []

for i in points:
    
    xa.append(i[0])
    ya.append(i[1])
    print(i)
    print('\n')
plt.plot(xa, ya, 'o')

plt.show()'''

def current_max_inside(line, points, area):
    count = 0

    for p in points:
        # point above line l
        if p[1] > line:
            # we know that area = (y_high - y_low)*(x_high - x_low), so we compute the needed values
            count_right = count_points_inside(p[0], (area + (p[0] * (p[1] - line))) / (p[1] - line), line, p[1])
            if count_right > count:
                count = count_right

            count_left = count_points_inside(((p[0] * (p[1] - line)) - area) / (p[1] - line), p[0], line, p[1])
            if count_left > count:
                count = count_left

        if p[1] < line:
            count_right = count_points_inside(p[0], (area + (p[0] * (line - p[1]))) / (line - p[1]), p[1], line)
            if count_right > count:
                count = count_right

            count_left = count_points_inside(((p[0] * (line - p[1])) - area) / (line - p[1]), p[0], p[1], line)
            if count_left > count:
                count = count_left

    return count

# returns the max number of points inside a box with area a
def max_points_in_box(points, area):
    # base case of recursion
    if len(points) <= 1:
        return 1
    
    med_index = len(points) // 2

    # line = c
    line = ((points[med_index][1] - points[med_index - 1][1]) / 2) + points[med_index - 1][1]

    # split set into two sub-sets of roughly equal number of points
    points_below = points[:med_index]
    points_above = points[med_index:]

    max_below = max_points_in_box(points_below, area)
    max_above = max_points_in_box(points_above, area)

    max_current = current_max_inside(line, points, area)

    return max(max_below, max_above, max_current)

print(max_points_in_box(points, 10000))
