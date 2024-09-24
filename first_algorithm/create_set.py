import random

P = []

def create_set(num_points, coord_range):

    for i in range(0, num_points):
        new = []
        new.append(random.uniform(coord_range[0], coord_range[1]))
        new.append(random.uniform(coord_range[0], coord_range[1]))

        P.append(new)

    return P
