plane = [[0] * 2001 for _ in range(2001)]
pos_x = 1000
pos_y = 1000
a_x1 = a_y1 = a_x2 = a_y2 = 0

for k in range(2):
    x1, y1, x2, y2 = map(int, input().split())
    if k == 0:
        a_x1, a_y1, a_x2, a_y2 = x1, y1, x2, y2
    for i in range(pos_x + x1, pos_x + x2):
        for j in range(pos_y + y1, pos_y + y2):
            if k == 1:
                if plane[i][j] == 1:
                    plane[i][j] = 0
            else:
                plane[i][j] = 1

x_start, x_end, y_start, y_end = 2001, 0, 2001, 0
for i in range(pos_x + a_x1, pos_x + a_x2):
    for j in range(pos_y + a_y1, pos_y + a_y2):
        if plane[i][j] == 1:
            x_start = min(x_start, i)
            y_start = min(y_start, j)
            x_end = max(x_end, i)
            y_end = max(y_end, j)

if (x_start, x_end, y_start, y_end) == (2001, 0, 2001, 0):
    print(0)
else:
    print((x_end - x_start + 1) * (y_end - y_start + 1))