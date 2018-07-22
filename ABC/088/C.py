c=[list(map(int,input().split())) for i in range(3)]
a=[]
b=[]
for i in range(3):
    a.append(c[i][0]-c[i][1])
    b.append(c[i][0]-c[i][2])
if len(set(a))==1 and len(set(b))==1:print("Yes")
else:print("No")

"""
c = [list(map(int, input().split())) for _ in range(3)]
a = []
b = []
a.append(0)
b.append(c[0][0])
b.append(c[0][1])
b.append(c[0][2])
a.append(c[1][0]-b[1])
a.append(c[2][0]-b[2])
for i in range(3):
    for j in range(3):
        if (a[i] + b[j] != c[i][j]):
            print("No")
            quit()
print("Yes")
"""
"""
for a1 in range(101):
    for a2 in range(101):
        for a3 in range(101):
            a.append(a1)
            a.append(a2)
            a.append(a3)
            b.append(c[0][0] - a1)
            b.append(c[0][1] - a1)
            b.append(c[0][2] - a1)
            flag = 1
            for i in range(0,3):
                for j in range(3):
                    if(a[i]+ b[j] != c[i][j]):
                        flag = 0
            if (flag):
                print("Yes")
print("No")
"""
