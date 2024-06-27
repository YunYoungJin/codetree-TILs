n, m, k = map(int, input().split())

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

go_down = True

for row in range(n - 1):
    for col in range(k, k + m):
        if grid[row + 1][col - 1] == 1:
            go_down = False
            break
    if not go_down:
        for col in range(k, k + m):
            grid[row][col - 1] = 1
        break

for row in grid:
    print(*row)