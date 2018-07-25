class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n+1)]
        self.rank = [0] * (n+1)

    def root(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.root(self.par[x])
            return self.par[x]

    def union(self, x, y):
        x = self.root(x)
        y = self.root(y)
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    def same(self, x, y):
        return self.root(x) == self.root(y)

N, K, L = map(int, input().split())
ufa = UnionFind(N)
ufb = UnionFind(N)

for _ in range(K):
    p,q = map(int,input().split())
    ufa.union(p,q)
for _ in range(L):
    r,s = map(int,input().split())
    ufb.union(r,s)

pairs = {}
for i in range(1,N+1):
    key = (ufa.root(i),ufb.root(i))
    if  key in pairs.keys():
        pairs[key] +=1
    else:
        pairs[key] =1
ans = []
for i in range(1,N+1):
    key = (ufa.root(i),ufb.root(i))
    ans.append(str(pairs[key]))
print(' '.join(ans))
