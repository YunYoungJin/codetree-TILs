plane = [[''] * 201 for _ in range(201)]
pos_x = 100
pos_y = 100

n = int(input())

for k in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    
    for i in range(pos_x + x1, pos_x + x2):
        for j in range(pos_y + y1, pos_y + y2):
            if k % 2 == 0:
                plane[i][j] = 'R' # 
            else:
                plane[i][j] = 'B'

blue_area = 0
for i in range(pos_x * 2):
    for j in range(pos_y * 2):
        if plane[i][j] == 'B':
            blue_area += 1
print(blue_area)