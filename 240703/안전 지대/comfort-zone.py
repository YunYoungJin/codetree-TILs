n, m = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

# 상, 하, 좌, 우
dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

def in_range(x, y):
    return (0 <= x and x < n) and (0 <= y and y < m)

def can_go(nx, ny, k):
    if not in_range(nx, ny):
        return False
    
    if visited[nx][ny] or (grid[nx][ny] <= k):
        return False

    return True

def dfs(curr_x, curr_y, k):
    for dx, dy in zip(dxs, dys):
        nx, ny = curr_x + dx, curr_y + dy

        if can_go(nx, ny, k):
            visited[nx][ny] = 1
            dfs(nx, ny, k)

safe_zones = []

for k in range(1, 100):
    visited = [[0] * m for _ in range(n)]
    zone = 0
    for i in range(n):
        for j in range(m):
            # 새 안전 영역을 발견 했을 때 탐색 진행
            if grid[i][j] > k and not visited[i][j]:
                zone += 1
                visited[i][j] = 1
                dfs(i, j, k)
    safe_zones.append((zone, k))

safe_zones.sort(key=lambda x: (-x[0], x[1]))
print(safe_zones[0][1], safe_zones[0][0])