n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

dxs, dys = [0, 1, 0, -1], [-1, 0, 1, 0]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

def can_go(x, y):
    if not in_range(x, y):
        return False
    if visited[x][y] or grid[x][y] == 0:
        return False
    return True

def dfs(x, y):
    visited[x][y] = True
    cnt = 1
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if can_go(nx, ny):
            cnt += dfs(nx, ny)
    return cnt

villages = []

for i in range(n):
    for j in range(n):
        if grid[i][j] == 1 and not visited[i][j]:
            villages.append(dfs(i, j))


print(len(villages))

for people in sorted(villages):
    print(people)