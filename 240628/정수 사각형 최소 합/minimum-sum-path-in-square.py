n = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

dp = [[0] * n for _ in range(n)]

dp[0][n - 1] = grid[0][n - 1]
for k in range(n - 2, -1, -1):
    dp[0][k] = grid[0][k] + dp[0][k + 1]
for k in range(1, n):
    dp[k][n - 1] = grid[k][n - 1] + dp[k - 1][n - 1]

for i in range(1, n):
    for j in range(n - 2, -1, -1):
        dp[i][j] = min(dp[i  - 1][j], dp[i][j + 1]) + grid[i][j]

print(dp[n - 1][0])