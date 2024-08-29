n = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

def in_range(x, y):
    return (0 <= x and x < n) and (0 <= y and y < n)

ans = 0
for i in range(1, n):
    for j in range(n):
        if grid[i - 1][j] == 0:
            ans += 1
            grid[i][j] = 1 - grid[i][j]

            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                ni, nj = i + dx, j + dy

                if in_range(ni, nj):
                    grid[ni][nj] = 1 - grid[ni][nj]

if grid[n - 1].count(0) > 0:
    print(-1)
else:
    print(ans)