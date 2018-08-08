import statistics

N = int(input())
A = list(map(int,input().split()))

for i in range(N):
    A[i] -= (i+1)

b = int(statistics.median(A))
print(sum(map(lambda x:abs(x-b), A)))
