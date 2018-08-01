N,W = map(int,input().split())
v_list = [[] for i in range(4)]

w_std,v = map(int,input().split())
v_list[0].append(v)
for i in range(N-1):
    wi,vi = map(int,input().split())
    v_list[wi-w_std].append(vi)
for i in range(4):
    v_list[i].sort(reverse=True)
    v_list[i].insert(0,0)

for i in range(4):
    if (len(v_list[i]) > 1):
        for j in range(1,len(v_list[i])):
            v_list[i][j] += v_list[i][j-1]

max_v = 0
for i in range(len(v_list[0])):
    for j in range(len(v_list[1])):
        for k in range(len((v_list[2]))):
            for l in range(len(v_list[3])):
                if (W >= i*w_std+j*(w_std+1)+k*(w_std+2)+l*(w_std+3)):
                    max_v = max(max_v,v_list[0][i]+v_list[1][j]+v_list[2][k]+v_list[3][l])
print(max_v)
