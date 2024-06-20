t, a, b = map(int, input().split())

line = [''] * 1001

for _ in range(t):
    c, x = input().split()
    line[int(x)] = c

ans = 0
for k in range(a, b + 1):
    d1, d2 = 1000, 1000
    for i in range(1, 1001):
        if line[i] == 'S':
            d1 = min(d1, abs(i-k))
        elif line[i] == 'N':
            d2 = min(d2, abs(i-k))
    if d1 <= d2:
        ans += 1
print(ans)