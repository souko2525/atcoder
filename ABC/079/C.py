N = list(input())
op = ['+','-']

for i in range(2):
    for j in range(2):
        for k in range(2):
                ans = 0
                if (op[i] == '+'):
                    ans = int(N[0]) + int(N[1])
                else:
                    ans = int(N[0]) - int(N[1])
                if (op[j] == '+'):
                    ans += int(N[2])
                else:
                    ans -= int(N[2])
                if (op[k] == '+'):
                    ans += int(N[3])
                else:
                    ans -= int(N[3])
                if (ans == 7):
                    print(N[0]+op[i]+N[1]+op[j]+N[2]+op[k]+N[3]+"=7")
                    quit()
