H,W = map(int,input().split())
#s = [['' for j in range(W+2)] for i in range(H+2)]
s = [list(input()) for i in range(H)]
x = [-1, 0, 1, 0]
y = [0, 1 , 0, -1]
for i in range(H):
    for j in range(W):
        if (s[i][j] == "#"):
            flag = False
            for d in range(4):
                if (i+y[d] >= 0 and i+y[d] < H and j+x[d] >= 0 and j+x[d] < W):
                    if(s[i+y[d]][j+x[d]] == "#"):
                        flag = True
            if (flag == False):
                print("No")
                quit()
print("Yes")
