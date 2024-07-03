n, m = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

visited = [[0] * m for _ in range(n)]

# 아래, 오른쪽
dxs = [1, 0]
dys = [0, 1]

def in_range(x, y):
    return (0 <= x and x < n) and (0 <= y and y < m)

def can_go(nx, ny):
    if not in_range(nx, ny):
        return False
    
    if visited[nx][ny] or (grid[nx][ny] == 0):
        return False

    return True

def dfs(curr_x, curr_y):
    for dx, dy in zip(dxs, dys):
        nx, ny = curr_x + dx, curr_y + dy

        if can_go(nx, ny):
            visited[nx][ny] = 1
            dfs(nx, ny)

visited[0][0] = 1
dfs(0, 0)

print(visited[n - 1][m - 1])