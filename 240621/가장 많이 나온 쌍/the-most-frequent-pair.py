n, m = map(int, input().split())

numbers = [
    tuple(map(int, input().split()))
    for _ in range(m)
]

ans = 0

for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        cnt = 0
        for a, b in numbers:
            if (i, j) == (a, b) or (i, j) == (b, a):
                cnt += 1
        ans = max(ans, cnt)

print(ans)