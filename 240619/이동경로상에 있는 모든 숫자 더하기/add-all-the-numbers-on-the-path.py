n, t = map(int, input().split())

commands = input()

board = [
    list(map(int, input().split()))
    for _ in range(n)
]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

# 0: 오른쪽, 1: 아래쪽, 2: 왼쪽, 3: 위쪽
dir_num = 3
dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]

x, y = n // 2, n // 2
ans = board[x][y]

for command in commands:
    if command == 'R':
        dir_num = (dir_num + 1) % 4
    elif command == 'L':
        dir_num = (dir_num + 3) % 4
    else:
        nx, ny = x + dxs[dir_num], y + dys[dir_num]
        
        # 격자를 벗어나게 되면
        if not in_range(nx, ny):
            continue
        
        ans += board[nx][ny]
        x, y = nx, ny
print(ans)