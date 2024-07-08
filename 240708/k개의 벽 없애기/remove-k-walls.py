import sys
from collections import deque

n, k = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())

wall_pos = [
    (i, j)
    for i in range(n)
    for j in range(n)
    if grid[i][j] == 1
]

selected_walls = []
ans = sys.maxsize

q = deque()
visited = [[-1] * n for _ in range(n)]
wall_moved_grid = [[-1] * n for _ in range(n)]

# 상, 하, 좌, 우
dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]


def initialize():
    for i in range(n):
        for j in range(n):
            wall_moved_grid[i][j] = grid[i][j]
            visited[i][j] = -1


def in_range(x, y):
    return (0 <= x and x < n) and (0 <= y and y < n)


def can_go(nx, ny):
    if not in_range(nx, ny):
        return False

    if (visited[nx][ny] != -1) or (wall_moved_grid[nx][ny] == 1):
        return False

    return True

def push(nx, ny, step):
    visited[nx][ny] = step
    q.append((nx, ny, step))

def bfs():
    # queue에 남은 것이 없을때까지 반복
    while q:
        x, y, step = q.popleft()

        # 4방향 확인
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy

            # 갈 수 있는 곳이라면
            # 새로 queue에 넣어주고 방문 여부 표시
            if can_go(nx, ny):
                push(nx, ny, step + 1)

wall_combs = []
tmp = []

# 현재까지 고른 벽의 개수 개수를 인자로
def select_wall(cnt):
    if cnt == k:
        comb = []
        for item in tmp:
            comb.append(item)
        wall_combs.append(comb)
        return

    for wall in wall_pos:
        if wall not in tmp:
            tmp.append(wall)
            select_wall(cnt + 1)
            tmp.pop()


select_wall(0)

for wall_comb in wall_combs:
    initialize()

    for r, c in wall_comb:
        wall_moved_grid[r][c] = 0

    push(r1 - 1, c1 - 1, 0)
    bfs()

    if visited[r2 - 1][c2 - 1] != -1:
        ans = min(ans, visited[r2 - 1][c2 - 1])

if ans == sys.maxsize:
    print(-1)
else:
    print(ans)