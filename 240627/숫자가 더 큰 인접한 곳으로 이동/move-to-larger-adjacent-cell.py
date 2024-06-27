n, r, c = map(int, input().split())
r, c = r - 1, c - 1

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

# 상, 하, 좌, 우
dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

def in_range(x, y):
    return (0 <= x and x < n) and (0 <= y and y < n)

visited = []

def check_move(r, c):
    pivot = grid[r][c]

    for i in range(4):
        nx, ny = r + dxs[i], c + dys[i]
        if in_range(nx, ny):
            if grid[nx][ny] > pivot:
                return nx, ny
    
    return r, c


while True:
    visited.append(grid[r][c])
    x, y = check_move(r, c)
    if (x, y) == (r, c):
        break
    else:
        r, c = x, y

print(*visited)