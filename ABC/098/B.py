N = int(input())
S = input()
ans = 0
for i in range(1,N):
   ans = max(ans,len(set(list(S[0:i])) & set(list(S[i:N]))))
print(ans)
