from collections import deque

n, m = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

# 상, 하, 좌, 우
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def in_range(x, y):
    return (0 <= x and x < n) and (0 <= y and y < m)

def is_edge_water(x, y):
    return x == 0 or y == 0 or x == n - 1 or y == m - 1

def bfs(start_points):
    queue = deque(start_points)
    visited = [[False] * m for _ in range(n)]
    for x, y in start_points:
        visited[x][y] = True

    melted_ice = set()
    
    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if in_range(nx, ny) and not visited[nx][ny]:
                if grid[nx][ny] == 1:
                    melted_ice.add((nx, ny))
                elif grid[nx][ny] == 0:
                    visited[nx][ny] = True
                    queue.append((nx, ny))

    for x, y in melted_ice:
        grid[x][y] = 0

    return len(melted_ice)

time = 0
last_melted = 0

while True:
    # 최외곽 물로부터 bfs 시작
    start_points = [(i, j) for i in range(n) for j in range(m) if grid[i][j] == 0 and is_edge_water(i, j)]
    melted_count = bfs(start_points)
    if melted_count == 0:
        break
    last_melted = melted_count
    time += 1

print(time, last_melted)