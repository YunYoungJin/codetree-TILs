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
            global cnt
            cnt += 1
            visited[nx][ny] = 1
            dfs(nx, ny)

villages = []

for i in range(n):
    for j in range(n):
        # 새 마을을 발견 했을 때 탐색 진행
        if grid[i][j] == 1 and not visited[i][j]:
            cnt = 1
            visited[i][j] = 1
            dfs(i, j)
            villages.append(cnt)


print(len(villages))

for people in sorted(villages):
    print(people)