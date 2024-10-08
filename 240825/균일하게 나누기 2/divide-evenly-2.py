import sys

n = int(input())
points = []
x_coords = set()
y_coords = set()

for _ in range(n):
    x, y = map(int, input().split())
    points.append((x, y))
    x_coords.add(x)
    y_coords.add(y)

x_coords = sorted(x_coords)
y_coords = sorted(y_coords)

ans = sys.maxsize

for a in range(x_coords[0] - 1, x_coords[-1], 2):
    for b in range(y_coords[0] - 1, y_coords[-1], 2):

        p1, p2, p3, p4 = 0, 0, 0, 0

        for x, y in points:
            if x > a and y > b:
                p1 += 1
            elif x < a and y > b:
                p2 += 1
            elif x < a and y < b:
                p3 += 1
            elif x > a and y < b:
                p4 += 1
            
        ans = min(ans, max(p1, p2, p3, p4))

print(ans)