n = int(input())
s = input()

cnt = 0
for i in range(len(s)):
    for j in range(i + 1, len(s)):
        for k in range(j + 1, len(s)):
            if s[i] == 'C' and s[j] == 'O' and s[k] == 'W':
                cnt += 1
print(cnt)