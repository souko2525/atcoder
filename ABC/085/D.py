import math

N, H = map(int, input().split())
a = []
b = []

for i in range(N):
    x, y = map(int, input().split())
    a.append(x)
    b.append(y)
max_a = max(a)
b = [i for i in b if i >= max_a]
b.sort()
b.reverse()
count = 0
for i in b:
    H -= i
    count +=1
    if H <= 0:
        print(count)
        quit()
print(math.ceil(H /max_a)+count)
