H,W = map(int,input().split())
c = [list(map(int, input().split())) for i in range(10)]
A = [list(map(int,input().split())) for  i in range(H)]
ans = 0

for k in range(10):
    for i in range(10):
        for j in range(10):
            c[i][j] = min(c[i][j],c[i][k]+c[k][j])

for i in range(H):
    for j in range(W):
        if A[i][j] == -1 or A[i][j] == 1:
            continue
        else:
            ans += c[A[i][j]][1]
print(ans)
