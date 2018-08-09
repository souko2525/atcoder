from itertools import accumulate

N = int(input())
A = list(map(int, input().split()))

sum_a = list(accumulate(A))
lft = 0
rgt = 2
t = sum_a[-1]
ans = t

for i in range(1,N-2):
    while sum_a[i] > sum_a[lft] + sum_a[lft+1]:
        lft += 1

    while t + sum_a[i] > sum_a[rgt] + sum_a[rgt+1]:
        rgt += 1
    print("--------")
    print(lft)
    print(rgt)
    p = sum_a[lft]
    q = sum_a[i] - p
    r = sum_a[rgt] - q - p
    s = t - r - q - p

    ans = min(ans, max(p,q,r,s) - min(p,q,r,s))

print(ans)
