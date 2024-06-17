n = int(input())
pos_x = 100
pos_y = 100
plane = [[0] * 201 for _ in range(201)]
area = 0

for _ in range(n):
    x1, y1 = map(int, input().split())
    for i in range(pos_x + x1, pos_x + x1 + 8):
        for j in range(pos_y + y1, pos_y + y1 + 8):
            plane[i][j] = 1
for line in plane:
    area += sum(line)
print(area)