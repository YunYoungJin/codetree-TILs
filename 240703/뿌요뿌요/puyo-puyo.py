n = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

visited = [[0] * n for _ in range(n)]

# 상, 하, 좌, 우
dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

def in_range(x, y):
    return (0 <= x and x < n) and (0 <= y and y < n)

def can_go(nx, ny, k):
    if not in_range(nx, ny):
        return False
    
    if visited[nx][ny] or (grid[nx][ny] != k):
        return False

    return True

def dfs(curr_x, curr_y, k):
    global cnt

    for dx, dy in zip(dxs, dys):
        nx, ny = curr_x + dx, curr_y + dy

        if can_go(nx, ny, k):
            cnt += 1
            visited[nx][ny] = 1
            dfs(nx, ny, k)

explosion = 0
block_size = 0

for k in range(1, 101):
    for i in range(n):
        for j in range(n):
            if can_go(i, j, k):
                cnt = 1
                visited[i][j] = 1
                dfs(i, j, k)
                if cnt >= 4:
                    explosion += 1
                block_size = max(block_size, cnt)

print(explosion, block_size)