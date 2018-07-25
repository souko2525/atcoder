H,W = map(int,input().split())
m = [list(input()) for _ in range(H)]
x = [1, 0, -1, 0, 1, -1, -1, 1]
y = [0, 1, 0, -1, 1, 1, -1, -1]

for i in range(H):
    for j in range(W):
        if(m[i][j] == "#"):
            continue
        count = 0
        for d in range(8):
            nx = j + x[d]
            ny = i + y[d]
            if((nx < 0 or W <= nx) or (ny < 0 or H <= ny)):
                continue
            if(m[ny][nx] == "#"):
                count +=1
        m[i][j]=str(count)
for i in range(H):
    print(''.join(m[i]))
