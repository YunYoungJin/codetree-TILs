n = int(input())
num_grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
direction_grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
r, c = map(lambda x: int(x) - 1, input().split())

# 방향 별 dx, dy
dxs = [-1, -1, 0, 1, 1, 1, 0, -1]
dys = [0, 1, 1, 1, 0, -1, -1, -1]

ans = 0

def in_range(x, y):
    return (0 <= x and x < n) and (0 <= y and y < n)

def can_go(x, y, pivot):
    if not in_range(x, y):
        return False
    
    if num_grid[x][y] <= pivot:
        return False
    
    return True

def get_max_move_cnt(x, y, cnt):
    global ans

    direction = direction_grid[x][y] - 1

    for i in range(1, n):
        nx, ny = x + dxs[direction] * i, y + dys[direction] * i

        if can_go(nx, ny, num_grid[x][y]):
            get_max_move_cnt(nx, ny, cnt + 1)
        else:
            ans = max(ans, cnt)


get_max_move_cnt(r, c, 0)
print(ans)