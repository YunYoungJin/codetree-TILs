n, m = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

max_sum = 0

# L자 블럭
for i in range(n - 1):
    for j in range(n - 1):
        tmp = grid[i][j] + grid[i][j + 1] + grid[i + 1][j] + grid[i + 1][j + 1]
        tmp -= min(grid[i][j], grid[i][j + 1], grid[i + 1][j], grid[i + 1][j + 1])
        max_sum = max(max_sum, tmp)

# I자 블럭
for i in range(n):
    for j in range(n - 2):
        tmp1 = grid[i][j] + grid[i][j + 1] + grid[i][j + 2]
        tmp2 = grid[j][i] + grid[j + 1][i] + grid[j + 2][i]
        max_sum = max(max_sum, tmp1, tmp2)

print(max_sum)