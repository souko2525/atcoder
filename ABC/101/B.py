N = input()
sum_n = sum(list(map(int, list(N))))
if int(N) % sum_n == 0:
    print("Yes")
else:
    print("No")
