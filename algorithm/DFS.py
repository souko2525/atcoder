class DFS:
    def __init__(self, N):
        self.N = N
        self.visited = []
        self.depth = [0 for i in range(N)]
        self.edge = [[] for i in range(N)]
        self.graph = [[False for i in range(N)] for j in range(N)]

    def dfs(self, v):
        self.visited[v] = False
        for i in range(self.N):
            if (self.graph[v][i] == False):
                continue
            if (self.visited[i]):
                continue
            self.dfs(i)

    def dfs2(self, v, p, d):
        self.depth[v] = d
        for e in range(self.edge[v]):
            if (e[0] == p):
                continue
            self.dfs2(e[0], v, d+e[1])
