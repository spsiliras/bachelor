from matplotlib import pyplot as plt
import bisect

# number of nearest x-coordinate points for each point of the set B
CLOSEST = 4

#returns the place of unfinished array where the point of set A
#belongs, accorning to Rl'y < ay
#returns -1 if it doesnt belong anywhere
def binary_search(low, high, x, unfinished):
    if high >= low:
        mid = (high+low) // 2
        if high==low:
            if unfinished[high][1] <= x:
                return high
            else:
                return low - 1
        
        elif unfinished[mid][1] > x:
            return binary_search(low, mid-1, x, unfinished)
        
        else:
            return binary_search(mid+1, high, x, unfinished)
        
    else:
        if unfinished[low][1] < x:
            return low
        else:
            return high

# case == 2: Pq-> where q in (P+ U P-*)
# case == 3: Pq<- where q in (P+ U P-*)
def lemma1_above(setP, case):
    # points of Rl' set which contains all visited B points
    # that do not have k points of visitedA
    unfinished = []

    # coontains the k closest points of each b point (if it has k closest)
    # because there will be points of b, which will be not have A points to the right of them
    solution = []

    # which variation of lemma1 i have to run
    if case == 2:
        # scan space from left to right
        setP.sort(key=lambda x:x[0])

    elif case == 3:
        # scan space from right to left
        setP.sort(key=lambda x:x[0], reverse=True)

    
    # sweep-line algorithm
    for i in setP:
        
        # its a B set point, so insert it to unfinished array (Rl' set point)
        # sorted by y-coordinate, so we can use array later to binary_search
        if i[2] == 1:
            point = []
            point.append(i[0])
            point.append(i[1])
            # use an empty array to mark the closest points later
            point.append([])

            # insert the point sorted by its y-coordinate
            bisect.insort(unfinished, point, key=lambda x:x[1])

        # a point which belongs to A n' B
        if i[2] == 0:
            
            # first consider it as a point of B
            p = []
            p.append(i[0])
            p.append(i[1])
            # use an empty array to mark the closest points later
            p.append([])

            # insert the point sorted by its y-coordinate
            bisect.insort(unfinished, p, key=lambda x:x[1])

            # then consider it as a point of A
            flag = binary_search(0, len(unfinished)-1, i[1], unfinished)

            if flag != -1:
                

                toDel = []
                for j in range(flag+1, len(unfinished)):
                    new_p = []
                    new_p.append(i[0])
                    new_p.append(i[1])
                    unfinished[j][2].append(new_p)

                    if len(unfinished[j][2]) == CLOSEST:
                        solution.append(unfinished[j])
                        toDel.append(j)

                for d in toDel[::-1]:  #reversed array toDel
                        
                    del unfinished[d]
                
    return solution, unfinished