class DFS:
    def __init__(self, N):
        self.N = N
        self.visited = []
        self.graph = [[False for i in range(N)] for j in range(N)]

    def dfs(self, v):
        self.visited[v] = False
        for i in range(self.N):
            if (self.graph[v][i] == False):
                continue
            if (self.visited[i]):
                continue
            self.dfs(i)
