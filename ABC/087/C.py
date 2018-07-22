N = int(input())
a = [list(map(int, input().split())) for i in range(2)]
ma = 0
for i in range(2):
    for j in range(1,N):
        a[i][j] += a[i][j-1]
for i in range(N):
    if(i==0):
        ma = max(ma, a[0][i]+ a[1][N-1])
    else:
        ma = max(ma, a[0][i]+ a[1][N-1]- a[1][i-1])
print(ma)
