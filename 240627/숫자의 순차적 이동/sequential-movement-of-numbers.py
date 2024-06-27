n, m = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

# 8 방향
dxs = [-1, -1, -1, 0, 0, 1, 1, 1]
dys = [-1, 0, 1, -1, 1, -1, 0, 1]


def in_range(x, y):
    return (0 <= x and x < n) and (0 <= y and y < n)


def simulate():

    for num in range(1, n * n + 1):
        cx, cy = -1, -1
        for i in range(n):
            for j in range(n):
                if grid[i][j] == num:
                    cx, cy = i, j
        
        tmp_max = 0
        tx, ty = 0, 0

        for dx, dy in zip(dxs, dys):
            nx, ny = cx + dx, cy + dy
            if in_range(nx, ny):
                if tmp_max < grid[nx][ny]:
                    tmp_max = grid[nx][ny]
                    tx, ty = nx, ny

        grid[cx][cy], grid[tx][ty] = grid[tx][ty], grid[cx][cy]


for _ in range(m):
    simulate()

for row in grid:
    print(*row)