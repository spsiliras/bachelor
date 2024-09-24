import random
import bisect

#returns the min area box for the current set Qi
#and an array with the points of the solution
def compute_best_top_box(array, q_top, q_bot, num_points):
    #keep the indexes 
    top_index = array.index(q_top)
    bot_index = array.index(q_bot)

    best = []

    #initially min box area is infinity
    minimum = float('inf')

    #that means that there is not a box which contains both
    #top and bottom point
    if(abs(top_index - bot_index) >= num_points):
        return [minimum, best]
    
    else:
        for i in range(0,len(array)+1-num_points):

            #the box it must contains both bottom and top points
            if((q_top in array[i:i+num_points]) and (q_bot in array[i:i+num_points])):
                new_min = (array[i+num_points-1][0] - array[i][0]) * (q_top[1] - q_bot[1])

                #check if the new area is less than the previous one
                if(new_min < minimum):
                    minimum = new_min
                    # store rectangle coordinates in form of [x_low, x_high, y_low, y_high]
                    best = [array[i][0], array[i+num_points-1][0], q_bot[1], q_top[1]].copy()

    return [minimum, best]

def compute_best_bot_box(array, q_bot, q_top, num_points):
    #keep the indexes 
    top_index = array.index(q_top)
    bot_index = array.index(q_bot)

    best = []

    #initially min box area is infinity
    minimum = float('inf')

    #that means that there is not a box which contains both
    #top and bottom point
    if(abs(top_index - bot_index) >= num_points):
        return [minimum, best]
    
    else:
        for i in range(0,len(array)+1-num_points):

            #the box it must contains both bottom and top points
            if((q_top in array[i:i+num_points]) and (q_bot in array[i:i+num_points])):
                new_min = (array[i+num_points-1][0] - array[i][0]) * (q_top[1] - q_bot[1])

                #check if the new area is less than the previous one
                if(new_min < minimum):
                    minimum = new_min
                    #update the points of the best current solution
                    best = [array[i][0], array[i+num_points-1][0], q_bot[1], q_top[1]].copy()

    return [minimum, best]

def lemma2(array, num_points):

    #Q_top sorted by increasing x-coordinate
    qTopSorted = []

    #Q_bot sorted by increasing x-coordinate
    qBotSorted = []

    #the point q
    q = []
    q.append(array[0][0])
    q.append(array[0][1])

    bestBox = []
    #initially the minimum value is equal to infinity
    m = float('inf')

    # then q is top point
    if(array[0][1] > array[1][1]):
        qTopSorted = sorted(array, key=lambda x:x[0])

        array = sorted(array, key=lambda x:x[1], reverse=True)
        

        while(len(array) >= num_points):
            #result is a list of the form of [minimum_value, solution_points] 
            result = compute_best_top_box(qTopSorted, q, array[len(array)-1], num_points)
            
            #update the total min and the current best points of solution
            if result[0] < m:
                m = result[0]

                bestBox = result[1].copy()

            #delete the point at the bottom of the set
            ind = qTopSorted.index(array[len(array)-1])
            qTopSorted.pop(ind)

            array.pop(len(array)-1)

    # q is bottom point of the set
    else:
        qBotSorted = sorted(array, key=lambda x:x[0])

        array = sorted(array, key=lambda x:x[1])

        while(len(array) >= num_points):
            result = compute_best_bot_box(qBotSorted, q, array[len(array)-1], num_points)

            if result[0] < m:
                m = result[0]

                bestBox = result[1].copy()

            ind = qBotSorted.index(array[len(array)-1])
            qBotSorted.pop(ind)

            array.pop(len(array)-1)

    return m, bestBox