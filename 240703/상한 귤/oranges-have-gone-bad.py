from collections import deque

n, k= map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

q = deque()
visited = [[0] * n for _ in range(n)]
step = [[-1] * n for _ in range(n)]

# 상, 하, 좌, 우
dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]


def in_range(x, y):
    return (0 <= x and x < n) and (0 <= y and y < n)


def can_go(nx, ny):
    if not in_range(nx, ny):
        return False

    if visited[nx][ny] or (grid[nx][ny] == 0):
        return False

    return True


def push(nx, ny, s):
    visited[nx][ny] = 1
    step[nx][ny] = s
    q.append((nx, ny))


def bfs():
    while len(q) != 0:
        curr_x, curr_y = q.popleft()
        
        for dx, dy in zip(dxs, dys):
            nx, ny = curr_x + dx, curr_y + dy

            if can_go(nx, ny):
                push(nx, ny, step[curr_x][curr_y] + 1)

for i in range(n):
    for j in range(n):
        if grid[i][j] == 2:
            push(i, j, 0)
bfs()

for i in range(n):
    for j in range(n):
        if visited[i][j] == 0 and grid[i][j] == 1:
            print(-2, end=' ')
        else:
            print(step[i][j], end=' ')
    print()