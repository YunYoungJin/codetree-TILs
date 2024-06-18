n = int(input())
x, y = 0, 0

# 동, 서, 남, 북
dx = [1, -1,  0, 0]
dy = [0,  0, -1, 1]

t = 0
arrival = False

for _ in range(n):
    c_dir, dist = input().split()
    dist = int(dist)
    
    # 각 방향에 맞는 번호를 붙여줍니다.
    if c_dir == 'E':
        move_dir = 0
    elif c_dir == 'W':
        move_dir = 1
    elif c_dir == 'S':
        move_dir = 2
    else:
        move_dir = 3

    for _ in range(dist):
        t += 1
        x += dx[move_dir]
        y += dy[move_dir]

        if (x, y) == (0, 0):
            arrival = True
            break
    if arrival:
        print(t)
        break
    
if not arrival:
    print(-1)