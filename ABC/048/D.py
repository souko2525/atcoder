s = list(input())
if(len(s)%2):
    count = False
else:
    count = True

if (s[0] == s[-1]):
    same = True
else:
    same = False

if (count^same):
    print("Second")
else:
    print("First")
