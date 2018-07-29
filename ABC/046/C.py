N = int(input())
A,B = 1,1

for _ in range(N):
    x,y = map(int,input().split())
    n = max((A-1)//x+1,(B-1)//y+1)
    A = n*x
    B = n*y
print(A+B)
