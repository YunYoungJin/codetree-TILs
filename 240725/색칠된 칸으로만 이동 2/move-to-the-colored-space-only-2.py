from collections import deque

m, n = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(m)
]
colored = [
    list(map(int, input().split()))
    for _ in range(m)    
]

colored_grid = []

for i in range(m):
    for j in range(n):
        if colored[i][j] == 1:
            colored_grid.append((i, j))

q = deque()
visited = [[False] * n for _ in range(m)]


def init():
    for i in range(m):
        for j in range(n):
            visited[i][j] = False


def in_range(x, y):
    return (0 <= x and x < m) and (0 <= y and y < n)


def can_go(x, y, pivot, d):
    if not in_range(x, y):
        return False

    if visited[x][y]:
        return False
    
    return abs(grid[x][y] - pivot) <= d


def push(x, y, pivot):
    visited[x][y] = True
    q.append((x, y, pivot))


def bfs(d):
    dxdys = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while q:
        x, y, pivot = q.popleft()

        for dx, dy in dxdys:
            nx, ny = x + dx, y + dy

            if can_go(nx, ny, pivot, d):
                push(nx, ny, grid[nx][ny])

    for i, j in colored_grid:
        if not visited[i][j]:
            return False
    
    return True


def is_possible(mid):
    init()
    r, c = colored_grid[0]
    push(r, c, grid[r][c])
    if bfs(mid):
        return True
    return False


left = 0
right = max(max(row) for row in grid) - min(min(row) for row in grid)
ans = right

while left <= right:
    mid = (left + right) // 2

    if is_possible(mid):
        right = mid - 1
        ans = min(ans, mid)
    else:
        left = mid + 1

print(ans)