N, M = map(int,input().split())
if (N*2 > M):
    print(M//2)
else:
    tmp = M - 2*N
    print(N+tmp//4)
