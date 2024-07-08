from collections import deque

n, h, m = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

shelter_pos = [
    (i, j)
    for i in range(n)
    for j in range(n)
    if grid[i][j] == 3
]

q = deque()
visited = [[-1] * n for _ in range(n)]

# 상, 하, 좌, 우
dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]


def in_range(x, y):
    return (0 <= x and x < n) and (0 <= y and y < n)


def can_go(nx, ny):
    if not in_range(nx, ny):
        return False

    if (visited[nx][ny] != -1) or (grid[nx][ny] == 1):
        return False

    return True


def push(nx, ny, step):
    visited[nx][ny] = step
    q.append((nx, ny, step))


def bfs():
    while len(q) != 0:
        curr_x, curr_y, step = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = curr_x + dx, curr_y + dy

            if can_go(nx, ny):
                push(nx, ny, step + 1)


for r, c in shelter_pos:
    push(r, c, 0)

bfs()

for i in range(n):
    for j in range(n):
        if grid[i][j] == 2:
            print(visited[i][j], end=' ')
        else:
            print(0, end=' ')
    print()