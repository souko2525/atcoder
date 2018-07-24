N, Y = map(int,input().split())
for i in range(2001):
    for j in range(2001):
        k = N - i -j
        if (k < 0):
            break
        if (10000 * i + 5000 * j + 1000 * k == Y):
            print(str(i) + ' ' + str(j) + ' ' + str(k))
            quit()
print("-1 -1 -1")
