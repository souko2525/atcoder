N,M = map(int,input().split())
ab = []
pre = 0
ans = 0
for _ in range(M):
    a,b = map(int,input().split())
    ab.append([a-1,b-1])
ab = sorted(ab, key=lambda x: x[1])
for i in ab:
    if i[0] >= pre:
        ans +=1
        pre = i[1]
print(ans)
