s = input()

cnt = 0

for i in range(len(s) - 3):
    for j in range(i + 2, len(s) - 1):
        if s[i] == '(' and s[i + 1] == '(' and\
        s[j] == ')' and s[j + 1] == ')':
            cnt += 1
print(cnt)