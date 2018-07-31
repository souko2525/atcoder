def abc(n,x):
    if(n==-1):
        return 0
    else:
        return n//x+1
a,b,x = map(int,input().split())
print(abc(b,x)-abc(a-1,x))
