n = int(input())

board = [
    list(input())
    for _ in range(n)
]

k = int(input())

# 0: 오른쪽, 1: 아래쪽, 2: 왼쪽, 3: 위쪽
direction = 0
dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]
x, y = 0, 0 
ans = 0

# 빛 진입방향
# 0: 위쪽, 1: 오른쪽, 2: 아래쪽, 3: 왼쪽
entry_dir = (k - 1) // n
entry_pos = (k - 1) % n

if entry_dir == 0:
    y += entry_pos
    direction = 1
elif entry_dir == 1:
    x += entry_pos
    y = n - 1
    direction = 2
elif entry_dir == 2:
    x = n - 1
    y = n - 1 - entry_pos
    direction = 3
else:
    x = n -1 - entry_pos
    direction = 0

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

while True:
    if board[x][y] == '\\':
        ans += 1
        # 빛이 왼쪽에서 들어오면
        if direction == 0:
            direction = (direction + 1) % 4 
            nx, ny = x + dxs[direction], y + dys[direction]
            if not in_range(nx, ny):
                break
            x, y = nx, ny
        # 빛이 위에서 들어오면
        elif direction == 1:
            direction = (direction + 3) % 4
            nx, ny = x + dxs[direction], y + dys[direction]
            if not in_range(nx, ny):
                break
            x, y = nx, ny
        # 빛이 오른쪽에서 들어오면
        elif direction == 2:
            direction = (direction + 1) % 4 
            nx, ny = x + dxs[direction], y + dys[direction]
            if not in_range(nx, ny):
                break
            x, y = nx, ny
        # 아래쪽에서 들어오면
        elif direction == 3:
            direction = (direction + 3) % 4
            nx, ny = x + dxs[direction], y + dys[direction]
            if not in_range(nx, ny):
                break
            x, y = nx, ny

    elif board[x][y] == '/':
        ans += 1
        # 빛이 왼쪽에서 들어오면
        if direction == 0:
            direction = (direction + 3) % 4 
            nx, ny = x + dxs[direction], y + dys[direction]
            if not in_range(nx, ny):
                break
            x, y = nx, ny
        # 빛이 위에서 들어오면
        elif direction == 1:
            direction = (direction + 1) % 4
            nx, ny = x + dxs[direction], y + dys[direction]
            if not in_range(nx, ny):
                break
            x, y = nx, ny
        # 빛이 오른쪽에서 들어오면
        elif direction == 2:
            direction = (direction + 3) % 4 
            nx, ny = x + dxs[direction], y + dys[direction]
            if not in_range(nx, ny):
                break
            x, y = nx, ny
        # 아래쪽에서 들어오면
        elif direction == 3:
            direction = (direction + 1) % 4
            nx, ny = x + dxs[direction], y + dys[direction]
            if not in_range(nx, ny):
                break
            x, y = nx, ny
print(ans)