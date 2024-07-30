n, m, k = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]


def apply_gravity(grid, n):
    for col in range(n):
        empty_row = n - 1
        for row in range(n - 1, -1, -1):
            if grid[row][col] != 0:
                grid[empty_row][col] = grid[row][col]
                if empty_row != row:
                    grid[row][col] = 0
                empty_row -= 1


def find_and_bomb(grid, n, m):
    has_bombed = False
    to_bomb = [[False] * n for _ in range(n)]

    for col in range(n):
        count = 1
        for row in range(1, n):
            if grid[row][col] == grid[row - 1][col] and grid[row][col] != 0:
                count += 1
            else:
                if count >= m:
                    for k in range(count):
                        to_bomb[row - 1 - k][col] = True
                count = 1

        if count >= m:
            for k in range(count):
                to_bomb[n - 1 - k][col] = True

    for row in range(n):
        for col in range(n):
            if to_bomb[row][col]:
                grid[row][col] = 0
                has_bombed = True

    apply_gravity(grid, n)
    return has_bombed


def rotate_90_clockwise(grid, n):
    new_grid = [[0] * n for _ in range(n)]
    for row in range(n):
        for col in range(n):
            new_grid[col][n - 1 - row] = grid[row][col]
    return new_grid


def count_bombs(grid, n):
    return sum(grid[row][col] != 0 for row in range(n) for col in range(n))


for _ in range(k):
    while find_and_bomb(grid, n, m):
        pass
    grid = rotate_90_clockwise(grid, n)
    apply_gravity(grid, n)

while find_and_bomb(grid, n, m):
    pass

print(count_bombs(grid, n))