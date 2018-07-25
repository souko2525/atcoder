class DFS:
    def __init__(self, N):
        self.N = N
        self.visited = [False for i in range(N)]
        self.graph = [[False for i in range(N)] for j in range(N)]

    def dfs(self, v):
        self.visited[v] = True
        for i in range(self.N):
            if (self.graph[v][i] == False):
                continue
            if (self.visited[i]):
                continue
            self.dfs(i)


N,M = map(int, input().split())
a = []
b = []
dfs = DFS(N)

for i in range(M):
    x,y = map(int, input().split())
    a.append(x-1)
    b.append(y-1)
    dfs.graph[a[i]][b[i]] = True
    dfs.graph[b[i]][a[i]] = True
ans = 0
for i in range(M):

    dfs.graph[a[i]][b[i]] = False
    dfs.graph[b[i]][a[i]] = False
    dfs.dfs(0)
    bridge = False
    for j in range(N):
        if (dfs.visited[j] == False):
            bridge = True
    if (bridge == True):
        ans +=1
    dfs.visited = [False for i in range(N)]
    dfs.graph[a[i]][b[i]] = True
    dfs.graph[b[i]][a[i]] = True
print(ans)
