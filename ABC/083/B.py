N,A,B = map(int,input().split())
ans=0

for i in range(1, N+1):
    tmp = sum(map(int,list(str(i))))
    if(tmp >= A and tmp <= B):
        ans+=i
print(ans)
