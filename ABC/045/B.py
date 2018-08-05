d={}
d["a"]=list(input())
d["b"]=list(input())
d["c"]=list(input())

t="a"
while 1:
    if not d[t]:
        print(t.upper())
        break
    s=d[t][0]
    d[t].pop(0)
    t=s
