S = input()
T = input()

for i in range(len(S)):
    if S == T:
        print("Yes")
        quit()
    S = S[-1] + S[0:-1]
print("No")
