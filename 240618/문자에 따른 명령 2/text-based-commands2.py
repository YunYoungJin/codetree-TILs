dx, dy = [1, 0, -1, 0], [0, -1, 0, 1] # E, S, W, N
dir_num = 3 
x, y = 0, 0

s = input()

for item in s:
    if item == 'L':
        dir_num = (dir_num + 3) % 4
    elif item == 'R':
        dir_num = (dir_num + 1) % 4
    else:
        x, y = x + dx[dir_num], y + dy[dir_num]

print(x, y)