a, b, c = map(int, input().split())

ans = 0

for i in range(c // b + 1):
    for j in range(c // a + 1):
        tmp = a * j + b * i
        if tmp <= c:
            ans = max(ans, tmp)

print(ans)