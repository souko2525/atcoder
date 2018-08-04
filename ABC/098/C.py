N = int(input())
S = list(input())

W = [ 1 if S[i]=='W' else 0 for i in range(N)]
E = [ 1 if S[i]=='E' else 0 for i in range(N)]

for i in range(1,N):
    W[i] = W[i-1]+W[i]
    E[-i-1] = E[-i] + E[-i-1]

ans = 3 * 10 **5

for i in range(N):
    if i == 0:
        ans = min(ans,E[1])
    elif i == N-1:
        ans = min(ans,W[N-2])
    else:
        ans = min(ans,W[i-1]+E[i+1])
print(ans)
