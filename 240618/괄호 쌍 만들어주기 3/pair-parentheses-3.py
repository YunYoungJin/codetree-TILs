s = input()

cnt = 0

for i in range(len(s)):
    if s[i] == '(':
        for j in range(i + 1, len(s)):
            if s[j] == ')':
                cnt += 1
print(cnt)