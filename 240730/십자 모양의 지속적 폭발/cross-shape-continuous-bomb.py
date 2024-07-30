n, m = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
cs = [
    int(input())
    for _ in range(m)
]


def in_bomb_range(x, y, center_x, center_y, bomb_range):
    return (x == center_x or y == center_y) and \
           abs(x - center_x) + abs(y - center_y) < bomb_range


def bomb(col):
    next_grid = [[0] * n for _ in range(n)]
    bomb_range = 0
    for row in range(n):
        if grid[row][col] != 0:
            bomb_range = grid[row][col]
            break

    # Step1. 폭탄이 터질 위치는 0으로 채워줍니다.
    for i in range(n):
        for j in range(n):
            if in_bomb_range(i, j, row, col, bomb_range):
                grid[i][j] = 0

    # Step2. 폭탄이 터진 이후의 결과를 next_grid에 저장합니다.
    for j in range(n):
        next_row = n - 1
        for i in range(n - 1, -1, -1):
            if grid[i][j]:
                next_grid[next_row][j] = grid[i][j]
                next_row -= 1

    # Step3. grid로 다시 값을 옮겨줍니다.
    for i in range(n):
        for j in range(n):
            grid[i][j] = next_grid[i][j]


for i in range(m):
    bomb(cs[i] - 1)

for i in range(n):
    for j in range(n):
        print(grid[i][j], end=" ")
    print()