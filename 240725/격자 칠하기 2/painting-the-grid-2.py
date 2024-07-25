from collections import deque

n = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
q = deque()
half = (n * n + 1) // 2
visited = [[False] * n for _ in range(n)]


def init():
    for i in range(n):
        for j in range(n):
            visited[i][j] = False


def in_range(x, y):
    return (0 <= x and x < n) and (0 <= y and y < n)


def can_go(x, y, pivot, d):
    return in_range(x, y) and not visited[x][y] and abs(grid[x][y] - pivot) <= d


def push(x, y, pivot):
    visited[x][y] = True
    q.append((x, y, pivot))


def bfs(d):
    dxdys = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    cnt = 0
    while q:
        x, y, pivot = q.popleft()
        cnt += 1

        for dx, dy in dxdys:
            nx, ny = x + dx, y + dy

            if can_go(nx, ny, pivot, d):
                push(nx, ny, grid[nx][ny])

    return cnt >= half


def is_possible(mid):
    init()
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                push(i, j, grid[i][j])
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