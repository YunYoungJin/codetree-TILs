n = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

# 해당 위치까지 이동중 적혀 있던 숫자 중 최솟 값
dp = [[0] * n for _ in range(n)]

dp[0][0] = grid[0][0]
for k in range(1, n):
    dp[k][0] = min(dp[k - 1][0], grid[k][0])
    dp[0][k] = min(dp[0][k - 1], grid[0][k])

for i in range(1, n):
    for j in range(1, n):
        dp[i][j] = min(max(dp[i - 1][j], dp[i][j - 1]), grid[i][j])

print(dp[n - 1][n - 1])