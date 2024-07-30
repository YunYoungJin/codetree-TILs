n = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

def in_bomb_range(x, y, center_x, center_y, bomb_range):
    return (x == center_x or y == center_y) and \
           abs(x - center_x) + abs(y - center_y) < bomb_range


def bomb_and_check(row, col):
    next_grid = [[0] * n for _ in range(n)]
    bomb_range = grid[row][col]

    for i in range(n):
        for j in range(n):
            if not in_bomb_range(i, j, row, col, bomb_range):
                next_grid[i][j] = grid[i][j]

    for c in range(n):
        empty_row = n - 1
        for r in range(n - 1, -1, -1):
            if next_grid[r][c] != 0:
                next_grid[empty_row][c] = next_grid[r][c]
                if empty_row != r:
                    next_grid[r][c] = 0
                empty_row -= 1

    cnt = 0
    for i in range(n):
        for j in range(n - 1):
            if next_grid[i][j] != 0 and next_grid[i][j] == next_grid[i][j + 1]:
                cnt += 1
            if next_grid[j][i] != 0 and next_grid[j][i] == next_grid[j + 1][i]:
                cnt += 1
    return cnt


ans = 0
for i in range(n):
    for j in range(n):
        ans = max(ans, bomb_and_check(i, j))

print(ans)