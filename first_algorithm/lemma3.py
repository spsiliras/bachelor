# This file returns 2 sets on this order
# p1 is the points above line l and symmetric points below l
# p2 is the points below line l and symmetric points above l

from lemma1_below import lemma1_below
from lemma1_above import lemma1_above

# separate the points of set P to two sets regarding their place to line l
# if above p_plus , if below p_min
def separate_set(P, l):
    # all points above the line
    p_plus = []

    # all points below the line
    p_minus = []

    for point in P:

        if point[1] > l:
            p_minus.append(find_symmetric(point, l))

            # insert a flag for use in lemma 1
            point.append(0)
            p_plus.append(point)

        else:
            p_plus.append(find_symmetric(point, l))

            # insert a flag for use in lemma 1
            point.append(0)
            p_minus.append(point)

    return p_plus, p_minus

# compute the symmetric of a point regarding to line l
def find_symmetric(point, l):
    new_point = []
    new_point.append(point[0])
    
    new_point.append(2*l - point[1])

    #insert a flag for use in lemma1
    new_point.append(1)

    return new_point

def lemma3(points, line, num_points):
    p_plus, p_minus = separate_set(points, line)

    # below right
    sol1, un1 = lemma1_below(p_minus, 0, num_points)
    br = sol1 + un1
    br.sort(key=lambda x:x[0])

    #print(br)

    # below left
    sol2, un2 = lemma1_below(p_minus, 1, num_points)
    bl = sol2 + un2
    bl.sort(key=lambda x:x[0])

    #print(bl)

    # above right
    sol3, un3 = lemma1_above(p_plus, 2, num_points)
    ar = sol3 + un3
    ar.sort(key=lambda x:x[0])

    #print(ar)

    # above left
    sol4, un4 = lemma1_above(p_plus, 3, num_points)
    al = sol4 + un4
    al.sort(key=lambda x:x[0])

    p = sorted(points, key=lambda x:x[0])
    setQ = []

    for i in range(0, len(p)):
        new = []
        new.append(p[i][0])
        new.append(p[i][1])

        v = br[i][2] + bl[i][2] + ar[i][2] + al[i][2]
        new.append(v)
        setQ.append(new)

    return setQ