import collections

N, K = map(int,input().split())
A = list(map(int, input().split()))
c = list(collections.Counter(A).values())
c.sort()
print(sum(c[0:len(c)-K]))
