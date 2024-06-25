n, m = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

max_sum = 0

# L자 블럭
for i in range(n - 1):
    for j in range(m - 1):
        tmp = grid[i][j] + grid[i][j + 1] + grid[i + 1][j] + grid[i + 1][j + 1]
        tmp -= min(grid[i][j], grid[i][j + 1], grid[i + 1][j], grid[i + 1][j + 1])
        max_sum = max(max_sum, tmp)

# I자 블럭 가로
for i in range(n):
    for j in range(m - 2):
        tmp = grid[i][j] + grid[i][j + 1] + grid[i][j + 2]
        max_sum = max(max_sum, tmp)

# I자 블럭 세로
for j in range(m):
    for i in range(n - 2):
        tmp = grid[i][j] + grid[i + 1][j] + grid[i + 2][j]
        max_sum = max(max_sum, tmp)

print(max_sum)