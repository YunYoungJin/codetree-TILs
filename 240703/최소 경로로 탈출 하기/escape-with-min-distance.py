from collections import deque

n, m = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
q = deque()
visited = [[0] * m for _ in range(n)]
step = [[-1] * m for _ in range(n)]

# 상, 하, 좌, 우
dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]


def in_range(x, y):
    return (0 <= x and x < n) and (0 <= y and y < m)


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

push(0, 0, 0)
bfs()

print(step[n - 1][m - 1])