from matplotlib import pyplot as plt
import random
import bisect

#number of nearest x-coordinate points for each point of the set B
CLOSEST = 3

#Give the number of points of set A
numA = 10
pointsA = []

#Give the number f points of set B
numB  = 5
pointsB = []

#points of set A to the left of line l (Al)
visitedA = []
#point of set B to the left of line l (Bl)
visitedB = []


#Contains all points (of setA and setB) sorted by its x-coordinate
#so we can use the sweep line algorithm
allSorted = []

#points of Rl' set which contains all visited B points
#that do not have k points of visitedA
unfinished = []

#coontains the k closest points of each b point (if it has k closest)
#because there will be points of b, which will be not have A points to the right of them
solution = []

#creates the two sets and sort them by x-coordinate
#fill the arrays:
#pointsA: with random data
#pointsB: with random data
#allSorted: with merged setA and setB, also sorted by x-coordinate
def create_dataset():
    
    #x and y random float in range (0, 40)
    for i in range(0, numA):
        point = []
        point.append(random.uniform(0,40))
        point.append(random.uniform(0,40))
        
        pointsA.append(point)

        #append 0 to find out later if its an A set point
        #or a B set point
        point.append(0)

        bisect.insort(allSorted, point, key=lambda x:x[0])

    for i in range(0, numB):
        point = []
        point.append(random.uniform(0,40))
        point.append(random.uniform(0,40))

        pointsB.append(point)

        #append 1 to find out later if its an A set point
        #or a B set point
        point.append(1)

        bisect.insort(allSorted, point, key=lambda x:x[0])

    return 0

#returns the place of unfinished array where the point of set A
#belongs, accorning to Rl'y < ay
#returns -1 if it doesnt belong anywhere
def binary_search(low, high, x):
    if high >= low:
        mid = (high+low) // 2
        if high==low:
            if unfinished[high][1] < x:
                return high
            else:
                return low - 1
        
        elif unfinished[mid][1] > x:
            return binary_search(low, mid-1, x)
        
        else:
            return binary_search(mid+1, high, x)
        
    else:
        if unfinished[low][1] < x:
            return low
        else:
            return high

def main():
    create_dataset()

    #sweep-line algorithm
    for i in allSorted:
        
        #its a B set point, so insert it to unfinished array (Rl' set point)
        #sorted by y-coordinate, so we can use array later to binary_search
        if i[2] == 1:
            point = []
            point.append(i[0])
            point.append(i[1])
            #use an empty array to mark the closest points later
            point.append([])

            #insert the point sorted by its y-coordinate
            bisect.insort(unfinished, point, key=lambda x:x[1])

        #its an Aset point
        if i[2] == 0:
            p = []
            p.append(i[0])
            p.append(i[1])

            #else, there is not a B set point, so this point of A set, doesn't belong anywhere
            if len(unfinished) != 0:
                flag = binary_search(0, len(unfinished)-1, i[1])
                if flag != -1:
                    toDel = []
                    for j in range(0, flag+1):
                        unfinished[j][2].append(p)
                        if len(unfinished[j][2]) == CLOSEST:
                            solution.append(unfinished[j])
                            toDel.append(j)

                    for d in toDel[::-1]:  #reversed array toDel
                        
                        del unfinished[d]
                
    return 0

main()

xa = []
ya = []
for i in pointsA:
    
    xa.append(i[0])
    ya.append(i[1])

print('\n')

xb = []
yb = []
for j in pointsB:
    
    xb.append(j[0])
    yb.append(j[1])

print('\n')

xs = []
ys = []
for k in solution:
    print(k)
    xs.append(k[0])
    ys.append(k[1])

plt.plot(xa,ya,'o')

plt.plot(xb,yb,'o')

plt.plot(xs,ys,'o')
plt.show()
