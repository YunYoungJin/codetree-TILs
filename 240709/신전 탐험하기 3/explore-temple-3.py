n, m = map(int, input().split())

infos = [0] + [
    tuple(map(int, input().split()))
    for _ in range(n)
]

dp = [[0] * m for _ in range(n + 1)]

for i in range(m):
    dp[1][i] = infos[1][i]

for i in range(2, n + 1):
    for j in range(m):
        for k in range(m):
            if j == k:
                continue
            dp[i][j] = max(dp[i][j], dp[i - 1][k] + infos[i][j])

print(max(dp[n]))