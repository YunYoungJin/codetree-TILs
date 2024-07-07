n = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

r, c, m1, m2, m3, m4, clockwise = map(int, input().split())
r, c = r - 1, c - 1

# 반시계 순회(0, 1 , 2 3)
# 시계 순회(1, 0, 3, 2)
dxs = [-1, -1, 1, 1]
dys = [1, -1, -1, 1]


def rotate_cw(r, c, p, q):
    temp = grid[r][c]

    x, y = r, c
    for _ in range(p):
        nx, ny = x + dxs[0], y + dys[0]
        grid[x][y] = grid[nx][ny]
        x, y = nx, ny
    
    for _ in range(q):
        nx, ny = x + dxs[1], y + dys[1]
        grid[x][y] = grid[nx][ny]
        x, y = nx, ny
    
    for _ in range(p):
        nx, ny = x + dxs[2], y + dys[2]
        grid[x][y] = grid[nx][ny]
        x, y = nx, ny
    
    for _ in range(q - 1):
        nx, ny = x + dxs[3], y + dys[3]
        grid[x][y] - grid[nx][ny]
        x, y = nx, ny
    
    grid[x][y] = temp


def rotate_ccw(r, c, p, q):
    temp = grid[r][c]

    x, y = r, c
    for _ in range(p):
        nx, ny = x + dxs[1], y + dys[1]
        grid[x][y] = grid[nx][ny]
        x, y = nx, ny
    
    for _ in range(q):
        nx, ny = x + dxs[0], y + dys[0]
        grid[x][y] = grid[nx][ny]
        x, y = nx, ny
    
    for _ in range(p):
        nx, ny = x + dxs[3], y + dys[3]
        grid[x][y] = grid[nx][ny]
        x, y = nx, ny
    
    for _ in range(q - 1):
        nx, ny = x + dxs[2], y + dys[2]
        grid[x][y] = grid[nx][ny]
        x, y = nx, ny
    
    grid[x][y] = temp

if clockwise:
    rotate_cw(r, c, m1, m2)
else:
    rotate_ccw(r, c, m2, m1)

for row in grid:
    print(*row)