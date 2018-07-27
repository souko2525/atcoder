class DFS:
    def __init__(self, N):
        self.N = N
        self.visited = []
        self.depth = [0 for i in range(N)]
        self.edge = [[] for i in range(N)]
        self.graph = [[False for i in range(N)] for j in range(N)]

    def dfs2(self, v, p, d):
        self.depth[v] = d
        for e in self.edge[v]:
            if (e[0] == p):
                continue
            self.dfs2(e[0], v, d+e[1])

N = int(input())
dfs = DFS(N)
for i in range(N-1):
    a,b,c = map(int, input().split())
    dfs.edge[a-1].append((b-1,c))
    dfs.edge[b-1].append((a-1,c))

Q,K = map(int,input().split())
dfs.dfs2(K-1,-1,0)
for _ in range(Q):
    x,y = map(int, input().split())
    print(dfs.depth[x-1]+dfs.depth[y-1])
