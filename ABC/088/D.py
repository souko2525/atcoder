class BFS():
    def __init__(self, H, W, maze):
        self.H = H
        self.W = W
        self.maze = maze
        self.distance = [[0 for i in range(self.W)] for j in range(self.H)]
        self.sx = 0
        self.sy = 0
        self.gx = W-1
        self.gy = H-1


    def bfs(self):
        queue = []
        queue.insert(0, (self.sx, self.sy))

        self.distance[self.sx][self.sy] = 0

        while len(queue):
            x, y = queue.pop()

            if x == self.gx and y == self.gy:
                break

            for i in range(0, 4):
                nx, ny = x + [1, 0, -1, 0][i], y + [0, 1, 0, -1][i]

                if (0 <= nx and nx < self.W and 0 <= ny and ny < self.H and self.maze[ny][nx] != '#' and self.distance[ny][nx] == 0):
                    queue.insert(0, (nx, ny))
                    self.distance[ny][nx] = self.distance[y][x] + 1
        return self.distance[self.gy][self.gx]

H, W = map(int, input().split())
maze = [list(input()) for _ in range(H)]
bfs = BFS(H,W,maze)
distance = bfs.bfs()
black = 0
for i in range(H):
    black += maze[i].count('#')

if distance == 0:
    print(-1)
else:
    print(H*W - (distance+1)-black)
