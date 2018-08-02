X,A,B = map(int,input().split())

if B -A <= 0:
    print("delicious")
else:
    if B-A <= X:
        print("safe")
    else:
        print("dangerous")
