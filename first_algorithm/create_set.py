import random

# the number of points of set P
num_points = 400
coord_range = [0, 400]
P = []

def create_set():

    for i in range(0, num_points):
        new = []
        new.append(random.uniform(coord_range[0], coord_range[1]))
        new.append(random.uniform(coord_range[0], coord_range[1]))

        P.append(new)

    return P
