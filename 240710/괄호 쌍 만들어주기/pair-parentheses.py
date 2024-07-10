s = list(input())

d = dict([('(', 0)])
ans = 0

for i in range(len(s) - 1):
    if s[i] == s[i + 1]:
        if s[i] == '(':
            d['('] += 1
        else:
            ans += d['(']

print(ans)