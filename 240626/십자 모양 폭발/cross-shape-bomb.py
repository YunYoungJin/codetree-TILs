n = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

r, c = map(int, input().split())
r, c = r - 1, c - 1

bp = grid[r][c]

for k in range(-bp + 1, bp):
    if 0 <= r + k and r + k <= n - 1:
        grid[r + k][c] = 0
    if 0 <= c + k and c + k <= n - 1:
        grid[r][c + k] = 0

temp = [[0] * n for _ in range(n)]

for col in range(n):
    temp_row = n - 1
    for row in range(n - 1, -1, -1):
        if grid[row][col] != 0:
            temp[temp_row][col] = grid[row][col]
            temp_row -= 1

for row in range(n):
    print(*temp[row])