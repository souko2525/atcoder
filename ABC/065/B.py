N = int(input())
a = []
for _ in range(N):
    a.append(int(input()))
index = 0
ans = 0
while N > 0:
    index = a[index]-1
    if (index == 1):
        print(ans+1)
        quit()
    N-=1
    ans+=1
print(-1)
