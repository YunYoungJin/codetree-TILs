n = int(input())

cards = [
    tuple(map(int, input().split()))
    for _ in range(2 * n)
]

dp = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    dp[i][0] = dp[i - 1][0] + cards[i - 1][0]
    dp[0][i] = dp[0][i - 1] + cards[i - 1][1]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        dp[i][j] = max(dp[i - 1][j] + cards[i + j - 1][0], dp[i][j - 1] + cards[i + j - 1][1])

print(dp[n][n])