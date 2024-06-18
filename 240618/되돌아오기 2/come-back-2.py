dx, dy = [1, 0, -1, 0], [0, -1, 0, 1] # E, S, W, N
dir_num = 3 
x, y = 0, 0

s = input()
t = 0
arrival = False

for item in s:
    t += 1
    if item == 'L':
        dir_num = (dir_num + 3) % 4
    elif item == 'R':
        dir_num = (dir_num + 1) % 4
    else:
        x, y = x + dx[dir_num], y + dy[dir_num]
        if (x, y) == (0, 0):
            arrival = True
            break
print(t if arrival else -1)