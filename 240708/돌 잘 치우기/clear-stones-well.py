from collections import deque

n, k, m = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
start_points = [
    tuple(map(int, input().split()))
    for _ in range(k)
]

stone_list = [
    (i, j)
    for i in range(n)
    for j in range(n)
    if grid[i][j] == 1
]


q = deque()
visited = [[False] * n for _ in range(n)]
stone_moved_grid = [[-1] * n for _ in range(n)]

# 상, 하, 좌, 우
dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]


def initialize():
    for i in range(n):
        for j in range(n):
            stone_moved_grid[i][j] = grid[i][j]
            visited[i][j] = False


def in_range(x, y):
    return (0 <= x and x < n) and (0 <= y and y < n)


def can_go(nx, ny):
    if not in_range(nx, ny):
        return False

    if visited[nx][ny] or (stone_moved_grid[nx][ny] == 1):
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


stone_combs = []
tmp = []


# 현재까지 돌의 개수 개수를 인자로
def select_stone(cnt):
    if cnt == m:
        comb = []
        for item in tmp:
            comb.append(item)
        stone_combs.append(comb)
        return

    for stone in stone_list:
        if stone not in tmp:
            tmp.append(stone)
            select_stone(cnt + 1)
            tmp.pop()


select_stone(0)

ans = 0
for stone_comb in stone_combs:
    initialize()

    for r, c in stone_comb:
        stone_moved_grid[r][c] = 0

    for r, c in start_points:
        push(r - 1, c - 1)
        bfs()

    tmp = 0
    for row in visited:
        tmp += row.count(1)

    ans = max(ans, tmp)

print(ans)