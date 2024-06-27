n, m, r, c = map(int, input().split())
r, c = r - 1, c - 1
grid = [[0] * n for _ in range(n)]
grid[r][c] = 1

# 상, 하, 좌, 우
dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

bomb_data = [(r, c)]

def in_range(x, y):
    return (0 <= x and x < n) and (0 <= y and y < n)

def already_exist(x, y):
    return grid[x][y] == 1

ans = 1
for t in range(1, m + 1):
    dist = 2 ** (t - 1)

    new_bomb_data = []
    for r, c in bomb_data:
        for dx, dy in zip(dxs, dys):
            nx, ny = r + dx * dist, c + dy * dist
            if in_range(nx, ny) and not already_exist(nx, ny):
                grid[nx][ny] = 1
                ans += 1
                new_bomb_data.append((nx, ny))

    for new_bomb in new_bomb_data:
        bomb_data.append(new_bomb)

print(ans)