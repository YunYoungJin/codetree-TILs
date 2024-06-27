n, m, t = map(int, input().split())

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

curr_beads = [[0] * n for _ in range(n)]

for _ in range(m):
    r, c = map(int, input().split())
    curr_beads[r - 1][c - 1] = 1

# 상, 하, 좌, 우
dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

def in_range(x, y):
    return (0 <= x and x < n) and (0 <= y and y < n)

def get_next_pos(r, c):
    x, y = r, c
    pivot = grid[r][c]

    for dx, dy in zip(dxs, dys):
        nx, ny = r + dx, c + dy
        if in_range(nx, ny):
            if grid[nx][ny] > pivot:
                x, y = nx, ny
                pivot = grid[nx][ny]
    
    return x, y

def move_all():
    after_move = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if curr_beads[i][j] == 1:
                nx, ny = get_next_pos(i, j)
                after_move[nx][ny] += 1

    for i in range(n):
        for j in range(n):
            if after_move[i][j] >= 2:
                curr_beads[i][j] = 0
            else:
                curr_beads[i][j] = after_move[i][j]

for _ in range(t):
    move_all()

ans = 0
for row in curr_beads:
    ans += row.count(1)
print(ans)