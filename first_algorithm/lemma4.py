from lemma3 import lemma3
from lemma2_new import lemma2

def lemma4():
    # preprocess and creation of the set P
    setQ = lemma3()
    
    for q in setQ:
        # prepare the item of setQ for lemma2
        p = []
        p.append(q[0])
        p.append(q[1])
        new = []
        new.append(p)
        new = new + q[2]
        
        print(new)
        if(len(new) > 4):
            print(lemma2(new)[0])
            print(lemma2(new)[1])
        print('\n')



lemma4()