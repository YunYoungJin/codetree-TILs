n = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

dp = [[0] * n for _ in range(n)]
visited = [[False] * n for _ in range(n)]

dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

def in_range(x, y):
    return (0 <= x and x < n) and (0 <= y and y < n)

def dfs(x, y):
    if dp[x][y] != 0:
        return dp[x][y]
    
    cnt = 1

    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy

        if in_range(nx, ny) and grid[nx][ny] > grid[x][y]:
            cnt = max(cnt, dfs(nx, ny) + 1)
    
    dp[x][y] = cnt

    return cnt

ans = 0
for i in range(n):
    for j in range(n):
       ans = max(ans, dfs(i, j))
print(ans)