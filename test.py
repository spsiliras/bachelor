a = [[1,2],[3,5],[6,8]]
b=[]

for i in range(0,5):
    a[2][1] = i
    b = a.copy()

print(b)