n, m = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

dp = [[0] * m for _ in range(n)]
dp[0][0] = 1

for i in range(n):
    for j in range(m):
        if dp[i][j] == 0:
            continue
        
        for p in range(i + 1, n):
            for q in range(j + 1, m):
                if grid[i][j] < grid[p][q]:
                    dp[p][q] = max(dp[p][q], dp[i][j] + 1)

print(max(max(row) for row in dp))