N,M = map(int,input().split())

def fa(N):
    p = 1
    for i in range(1,N+1):
        p = (p * i)%(10**9+7)
    return p
if abs(N-M) > 1:
    print(0)
elif abs(N-M) == 1:
    print((fa(N)*fa(M))%(10**9+7))
else:
    print((2*fa(N)*fa(M))%(10**9+7))
