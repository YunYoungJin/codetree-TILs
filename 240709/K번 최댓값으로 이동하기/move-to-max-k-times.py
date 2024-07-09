from collections import deque

n, k = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
r, c = map(lambda x: int(x) - 1, input().split())
visited = [[False] * n for _ in range(n)]
pivot = grid[r][c]
q = deque()

dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]


def initialize():
    for i in range(n):
        for j in range(n):
            visited[i][j] = False


def in_range(x, y):
    return (0 <= x and x < n) and (0 <= y and y < n)


def can_go(x, y, pivot):
    if not in_range(x, y):
        return False

    if visited[x][y] or (grid[x][y] >= pivot):
        return False

    return True


def push(x, y):
    visited[x][y] = True
    q.append((x, y))


def bfs(pivot):
    next_pivot = 0

    while q:
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy

            if can_go(nx, ny, pivot):
                push(nx, ny)
                next_pivot = max(next_pivot, grid[nx][ny])

    return next_pivot


def select_next_pos(pivot):
    for i in range(n):
        for j in range(n):
            if visited[i][j] and grid[i][j] == pivot:
                return i, j


for _ in range(k):
    initialize()

    no_more_go = True
    for dx, dy in zip(dxs, dys):
        nx, ny = r + dx, c + dy

        if can_go(nx, ny, pivot):
            no_more_go = False

    if no_more_go:
        break

    push(r, c)
    pivot = bfs(pivot)

    r, c = select_next_pos(pivot)

print(r + 1, c + 1)