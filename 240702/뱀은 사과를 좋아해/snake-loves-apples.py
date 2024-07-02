from collections import deque

n, m, k = map(int, input().split())
grid = [[0] * n for _ in range(n)]

# 사과 표시
for _ in range(m):
    x, y = map(int, input().split())
    grid[x - 1][y - 1] = 2

directions = [
    tuple(input().split())
    for _ in range(k)
]

# 상, 하, 좌, 우
dir_map = {'U' : 0, 'D' : 1, 'L' : 2, 'R' : 3}
dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

def in_range(x, y):
    return (0 <= x and x < n) and (0 <= y and y < n)

t = 0
x, y = 0, 0
grid[x][y] = 1
snake = deque([(x, y)])

for d, p in directions:
    end = False
    for _ in range(int(p)):
        t += 1
        nx, ny = x + dxs[dir_map[d]], y + dys[dir_map[d]]
        # 새 머리 위치가 격자를 벗어나면
        if not in_range(nx, ny):
            end = True
            break

        # 사과가 아니면 바로 꼬리 제거
        if grid[nx][ny] != 2:
            a, b = snake.pop()
            grid[a][b] = 0

        if (nx, ny) in snake:
            end = True
            break

        # 머리의 새로운 위치 추가
        x, y = nx, ny
        grid[x][y] = 1
        snake.appendleft((nx, ny))

    if end:
        break

print(t)