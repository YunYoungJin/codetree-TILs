n, m = map(int, input().split())
board = [[0] * n for _ in range(n)]

# 위칸, 오른칸, 아래칸, 왼칸
dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

for _ in range(m):
    r, c = map(int, input().split())
    r, c = r -1, c -1
    board[r][c] = 1

    cnt = 0
    for dx, dy in zip(dxs, dys):
        nx, ny = r + dx, c + dy
        if in_range(nx, ny) and board[nx][ny] == 1:
            cnt += 1
    if cnt == 3:
        print(1)
    else:
        print(0)