import math

a, b = map(str, input().split())
tmp = int(a+b)
if math.floor(math.sqrt(int(a+b)))**2 == tmp:
    print("Yes")
else:
    print("No")
