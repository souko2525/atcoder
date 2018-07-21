N, K = map(int, input().split())
board = [[0 for i in range(2*K+10)] for i in range(2*K+10)]
sum = 0
white=0

for i in range(N):
    x,y,c = input().split()
    x = int(x) % (2*K)
    y = int(y) % (2*K)
    if(c=='B'):
        board[x+1][y+1]+=1
        sum+=1
    if (c=='W'):
        board[x+1][y+1]-=1
        sum-=1
        white+=1

for i in range(2*K):
    for j in range(2*K):
        board[i][j] += board[i][j-1]

for i in range(2*K):
    for j in range(2*K):
        board[i][j] += board[i-1][j]
ma = -1 << 25
for i in range(K):
    for j in range(K):
        a = board[i][j]
        b = board[i+K][j+K] - board[i+K][j] - board[i][j+K] + board[i][j]
        c = board[2*K][j] - board[i+K][j]
        d = board[i][2*K] - board[i][j+K]
        e = board[2*K][2*K] - board[2*K][j+K] - board[i+K][2*K] + board[i+K][j+K]
        tmp = a + b + c + d + e
        ma = max(ma, max(tmp, sum - tmp))
print(ma)
