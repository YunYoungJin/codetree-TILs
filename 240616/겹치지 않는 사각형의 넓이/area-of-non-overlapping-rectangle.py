plane = [[0] * 2000 for _ in range(2000)]
pos_x = 1000
pos_y = 1000
area = 0

for k in range(3):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(pos_x + x1, pos_x + x2):
        for j in range(pos_y + y1, pos_y + y2):
            if k == 2:
                if plane[i][j] == 1:
                    area -= 1
            else:
                plane[i][j] = 1
                area += 1
print(area)