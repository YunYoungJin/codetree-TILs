from collections import deque

n, k, u, d = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

city_list = [
    (i, j)
    for i in range(n)
    for j in range(n)
]

start_points = []

q = deque()
visited = [[False] * n for _ in range(n)]


# 상, 하, 좌, 우
dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]


def initialize():
    for i in range(n):
        for j in range(n):
            visited[i][j] = False


def in_range(x, y):
    return (0 <= x and x < n) and (0 <= y and y < n)


def can_go(x, y, nx, ny):
    if not in_range(nx, ny):
        return False

    if visited[nx][ny]:
        return False

    diff = abs(grid[x][y] - grid[nx][ny]) 
    if diff < u or d < diff:
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

            if can_go(curr_x, curr_y, nx, ny):
                push(nx, ny)

tmp = []

# 현재까지 선택한 도시의 개수를 인자로
def select_city(cnt):
    if cnt == k:
        comb = []
        for item in tmp:
            comb.append(item)
        start_points.append(comb)
        return

    for city in city_list:
        if city not in tmp:
            tmp.append(city)
            select_city(cnt + 1)
            tmp.pop()


select_city(0)

ans = 0
for city_comb in start_points:
    initialize()

    for r, c in city_comb:
        push(r, c)
        bfs()

    tmp = 0
    for row in visited:
        tmp += row.count(1)

    ans = max(ans, tmp)

print(ans)