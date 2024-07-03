from collections import deque

n, k = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
start_points = [
    tuple(map(int, input().split()))
    for _ in range(k)
]

q = deque()
visited = [[0] * n for _ in range(n)]

# 상, 하, 좌, 우
dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]


def in_range(x, y):
    return (0 <= x and x < n) and (0 <= y and y < n)


def can_go(nx, ny):
    if not in_range(nx, ny):
        return False

    if visited[nx][ny] or (grid[nx][ny] == 1):
        return False

    return True


def push(nx, ny):
    visited[nx][ny] = 1
    q.append((nx, ny))


def bfs():
    while len(q) != 0:
        curr_x, curr_y = q.popleft()
        
        for dx, dy in zip(dxs, dys):
            nx, ny = curr_x + dx, curr_y + dy

            if can_go(nx, ny):
                push(nx, ny)

for r, c in start_points:
    push(r - 1, c - 1)
    bfs()

ans = 0
for row in visited:
    ans += row.count(1)
print(ans)