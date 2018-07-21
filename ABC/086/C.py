n = int(input())
pre_t,pre_x,pre_y=0, 0, 0
for i in range(n):
    t, x, y = map(int, input().split())
    d_t = t-pre_t
    d_x = abs(x-pre_x)
    d_y = abs(y-pre_y)
    if d_x + d_y > d_t or (d_x + d_y + d_t) % 2:
        print("No")
        quit()
    pre_t,pre_x,pre_y=t, x, y
print("Yes")
