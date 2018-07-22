N = int(input())
a = list(map(int,input().split()))
a.sort(reverse=True)
print(sum(a[0:N:2])-sum(a[1:N:2]))
