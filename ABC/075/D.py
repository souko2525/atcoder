N,K = map(int,input().split())
point = []
y_list = []

for _ in range(N):
    x,y = map(int, input().split())
    point.append((x,y))
    y_list.append(y)
point = sorted(point,key=lambda tup: tup[0])
y_list.sort()
min_area = (y_list[N-1] - y_list[0]) * (point[N-1][0] - point[0][0])

for by in range(N):
    for ty in range(by+1,N):
        size=0
        idx = [0 for _ in range(N)]
        for i in range(N):
            if (y_list[by] <= point[i][1] and y_list[ty] >= point[i][1]):
                idx[size] = i
                size +=1
        lb = 0
        while(lb + K -1 < size):
            min_area = min(min_area, (y_list[ty] - y_list[by]) * (point[idx[lb + K - 1]][0] - point[idx[lb]][0]))
            lb+=1
print(min_area)
