n=int(input())
a=[int(i) for i in input().split()]

ans=0
b=0
j=0
for i in range(n):
    print("-----------")
    print(j)
    while j<n and b^a[j]==b+a[j]:
        b^=a[j]
        print(b, a[j])
        j=j+1
    ans += j-i
    b^=a[i]
print(ans)
