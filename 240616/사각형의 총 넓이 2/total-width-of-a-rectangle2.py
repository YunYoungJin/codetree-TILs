n = int(input())

plane = [[0] * 200 for _ in range(200)]
pos_x = 100
pos_y = 100

for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(pos_x + x1, pos_x + x2):
        for j in range(pos_y + y1, pos_y + y2):
            plane[i][j] = 1
square = 0
for line in plane:
    square += sum(line)
print(square)