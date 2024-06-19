n, m = map(int, input().split())

board = [
    list(input())
    for _ in range(n)
]

# 오른쪽 위, 오른쪽, 오른쪽 아래, 아래, 왼쪽 아래, 왼쪽, 왼쪽 위, 위
directions = [(-1, 1), (0, 1), (1, 1), (1,0), (1, -1), (0, -1), (-1, -1), (-1, 0)]

def in_range(x, y):
    return (0 <= x and x < n) and (0 <= y and y < m)

cnt = 0

for i in range(n):
    for j in range(m):
        if board[i][j] == 'L':
            for direction in directions:
                found = True
                x, y = i, j
                dx, dy = direction
                for _ in range(2):
                    nx = x + dx
                    ny = y + dy
                    if not in_range(nx, ny):
                        found = False
                        break
                    if board[nx][ny] != 'E':
                        found = False
                        break
                    x, y = nx, ny
                if found:
                    cnt += 1
print(cnt)