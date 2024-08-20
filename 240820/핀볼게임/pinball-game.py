n = int(input())

board = [
    list(map(int, input().split()))
    for _ in range(n)
]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

# 0: 오른쪽, 1: 아래쪽, 2: 왼쪽, 3: 위쪽
direction = 0
dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]
ans = 0

for k in range(4 * n):
    # 구슬 진입방향
    entry_dir = k // n
    entry_pos = k % n
    time = 0
    x, y = 0, 0 

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
        x = n - 1 - entry_pos
        direction = 0

    while True:
        time += 1
        if board[x][y] == 2:
            # 구슬이 왼쪽에서 들어오면
            if direction == 0:
                direction = (direction + 1) % 4 
            # 구슬이 위에서 들어오면
            elif direction == 1:
                direction = (direction + 3) % 4
            # 구슬이 오른쪽에서 들어오면
            elif direction == 2:
                direction = (direction + 1) % 4 
            # 아래쪽에서 들어오면
            elif direction == 3:
                direction = (direction + 3) % 4
        elif board[x][y] == 1:
            # 구슬이 왼쪽에서 들어오면
            if direction == 0:
                direction = (direction + 3) % 4 
            # 구슬이 위에서 들어오면
            elif direction == 1:
                direction = (direction + 1) % 4
            # 구슬이 오른쪽에서 들어오면
            elif direction == 2:
                direction = (direction + 3) % 4 
            # 아래쪽에서 들어오면
            elif direction == 3:
                direction = (direction + 1) % 4
        
        nx, ny = x + dxs[direction], y + dys[direction]
        if not in_range(nx, ny):
            time += 1
            break
        x, y = nx, ny            
    
    ans = max(ans, time)

print(ans)