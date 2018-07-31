N,x = map(int,input().split())
a = list(map(int,input().split()))
a_sum = sum(a)
if (a[0]>x):
    a[0] = x
for i in range(N-1):
    if (a[i]+a[i+1] > x):
        a[i+1] -= max(0,(a[i]+a[i+1]-x))
    else:
        pass
print(a_sum-sum(a))
