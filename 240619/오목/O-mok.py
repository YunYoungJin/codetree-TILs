import sys

board = [
    list(map(int, input().split()))
    for _ in range(19)
]

# 오른쪽 위, 오른쪽, 오른쪽 아래, 아래
directions = [(-1, 1), (0, 1), (1, 1), (1,0)]

def in_range(x, y):
    return (0 <= x and x < 19) and (0 <= y and y < 19)

for i in range(19):
    for j in range(19):
        if board[i][j] != 0:
            for direction in directions:
                x, y = i, j
                dx, dy = direction
                cnt = 1
                while True:
                    nx = x + dx
                    ny = y + dy
                    if not in_range(nx, ny):
                        break
                    if board[x][y] != board[nx][ny]:
                        break
                    cnt += 1
                    x, y = nx, ny
                if cnt == 5:
                    print(board[x][y])
                    print(i + 2 * dx + 1, j + 2 * dy + 1)
                    sys.exit()
print(0)