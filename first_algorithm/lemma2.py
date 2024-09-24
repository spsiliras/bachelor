import random
import bisect

#the number of points of the best box
K = 4


def create_sets(numPoints, coord, Qset, qPoint, qTop, qBot):
    
    #create -numPoints- points in place (coord[0],coord[1])x(coord[0],coord[1])
    for i in range(0, numPoints):
        point = []
        point.append(random.uniform(coord[0],coord[1]))
        point.append(random.uniform(coord[0],coord[1]))

        Qset.append(point)

    #choose a random point of Q as q (q belongs at the bottom nad the top of the box)
    index = random.randint(0, numPoints-1)
    
    qPoint.append(Qset[index][0])
    qPoint.append(Qset[index][1])

    qTop.append(qPoint)
    qBot.append(qPoint)

    #sort the random points
    for i in Qset:
        #if q is top point, sort the points with smaller y-coordinate by descending order
        if i[1] < qPoint[1]:
            bisect.insort(qTop, i, key=lambda x:-x[1])
        
        #if q is bottom point, sort the points with greater y-coordinate by ascending order
        elif i[1] > qPoint[1]:
            bisect.insort(qBot, i, key=lambda x:x[1])



#returns the min area box for the current set Qi
#and an array with the points of the solution
def compute_best_top_box(array, q_top, q_bot):
    #keep the indexes 
    top_index = array.index(q_top)
    bot_index = array.index(q_bot)

    best = []

    #initially min box area is infinity
    minimum = float('inf')

    #that means that there is not a box which contains both
    #top and bottom point
    if(abs(top_index - bot_index) >= K):
        return [minimum, best]
    
    else:
        for i in range(0,len(array)+1-K):

            #the box it must contains both bottom and top points
            if((q_top in array[i:i+K]) and (q_bot in array[i:i+K])):
                new_min = (array[i+K-1][0] - array[i][0]) * (q_top[1] - q_bot[1])

                #check if the new area is less than the previous one
                if(new_min < minimum):
                    minimum = new_min
                    #update the points of the best current solution
                    best = array[i:i+K].copy()

    return [minimum, best]

def compute_best_bot_box(array, q_bot, q_top):
    #keep the indexes 
    top_index = array.index(q_top)
    bot_index = array.index(q_bot)

    best = []

    #initially min box area is infinity
    minimum = float('inf')

    #that means that there is not a box which contains both
    #top and bottom point
    if(abs(top_index - bot_index) >= K):
        return [minimum, best]
    
    else:
        for i in range(0,len(array)+1-K):

            #the box it must contains both bottom and top points
            if((q_top in array[i:i+K]) and (q_bot in array[i:i+K])):
                new_min = (array[i+K-1][0] - array[i][0]) * (q_top[1] - q_bot[1])

                #check if the new area is less than the previous one
                if(new_min < minimum):
                    minimum = new_min
                    #update the points of the best current solution
                    best = array[i:i+K].copy()

    return [minimum, best]

def main():

    #the number of points of Q set
    num = 40
    #the range of Q set points (here x->0...40 and y->0...40)
    coordinates = [0,40]
    #Q set of points
    Q = []

    #contain the points in the case of q belongs to top
    qTop = []
    #Q_top sorted by increasing x-coordinate
    qTopSorted = []

    #contains the points in the case of q belongs to bottom
    qBot = []
    #Q_bot sorted by increasing x-coordinate
    qBotSorted = []

    #the point q
    q = []

    bestBox = []

    create_sets(num, coordinates, Q, q, qTop, qBot)

    qTopSorted = sorted(qTop, key=lambda x:x[0])
    qBotSorted = sorted(qBot, key=lambda x:x[0])

    #initially the minimum value is equal to infinity
    m = float('inf')

    while(len(qTop) >= K):
        #result is a list of the form of [minimum_value, solution_points] 
        result = compute_best_top_box(qTopSorted, q, qTop[len(qTop)-1])
        
        #update the total min and the current best points of solution
        if result[0] < m:
            m = result[0]

            bestBox = result[1].copy()

        #delete the point at the bottom of the set
        ind = qTopSorted.index(qTop[len(qTop)-1])
        qTopSorted.pop(ind)

        qTop.pop(len(qTop)-1)

    while(len(qBot) >= K):
        result = compute_best_bot_box(qBotSorted, q, qBot[len(qBot)-1])

        if result[0] < m:
            m = result[0]

            bestBox = result[1].copy()

        ind = qBotSorted.index(qBot[len(qBot)-1])
        qBotSorted.pop(ind)

        qBot.pop(len(qBot)-1)

    print(m)
    print(q)
    print('\n')
    print(bestBox)

main()


    

