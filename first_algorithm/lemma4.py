from lemma3 import lemma3
from lemma2_new import lemma2

def lemma4(points, line, num_points):
    # preprocess and creation of the set P
    setQ = lemma3(points, line, num_points)
    # area = a big value initially so we can minimize it later
    area = float('inf')
    # best box === box with the minimum area and most points
    best_box = []
    
    for q in setQ:
        # prepare the item of setQ for lemma2
        p = []
        p.append(q[0])
        p.append(q[1])
        new = []
        new.append(p)
        new = new + q[2]
        
        if(len(new) >= num_points):
            area_new, best_box_new = lemma2(new, num_points)
            if area_new < area:
                area = area_new
                best_box = best_box_new.copy()

    return area, best_box