words = ["dream", "dreamer", "erase","eraser"]
reverse_words = []
for word in words:
    reverse_words.append(word[::-1])
S = input()
S = S[::-1]

while len(S) !=0:
    flag = 0
    for word in reverse_words:
        if S.startswith(word):
            S = S[len(word):]
            flag=1
            break
    if (not flag):
        print("NO")
        quit()
print("YES")
