import sys
input = sys.stdin.readline
from bisect import bisect_left, bisect_right

n, q = map(int, input().split())
points = []
queries = []
x_coords = set()
y_coords = set()

for _ in range(n):
    x, y = map(int, input().split())
    points.append((x, y))
    x_coords.add(x)
    y_coords.add(y)

for _ in range(q):
    x1, y1, x2, y2 = map(int, input().split())
    queries.append((x1, y1, x2, y2))
    x_coords.add(x1)
    x_coords.add(x2)
    y_coords.add(y1)
    y_coords.add(y2)

x_sorted = sorted(x_coords)
y_sorted = sorted(y_coords)

x_map = {x: i for i, x in enumerate(x_sorted)}
y_map = {y: i for i, y in enumerate(y_sorted)}

max_x = len(x_sorted)
max_y = len(y_sorted)

# Create the 2D grid for prefix sum
grid = [[0] * (max_y + 1) for _ in range(max_x + 1)]

for x, y in points:
    cx = x_map[x]
    cy = y_map[y]
    grid[cx][cy] += 1

for i in range(max_x + 1):
    for j in range(max_y + 1):
        if i > 0:
            grid[i][j] += grid[i - 1][j]
        if j > 0:
            grid[i][j] += grid[i][j - 1]
        if i > 0 and j > 0:
            grid[i][j] -= grid[i - 1][j - 1]

for x1, y1, x2, y2 in queries:
    cx1 = bisect_left(x_sorted, x1)
    cy1 = bisect_left(y_sorted, y1)
    cx2 = bisect_right(x_sorted, x2) - 1
    cy2 = bisect_right(y_sorted, y2) - 1

    if cx1 > cx2 or cy1 > cy2:
        print(0)
        continue
    
    total = grid[cx2][cy2]
    if cx1 > 0:
        total -= grid[cx1 - 1][cy2]
    if cy1 > 0:
        total -= grid[cx2][cy1 - 1]
    if cx1 > 0 and cy1 > 0:
        total += grid[cx1 - 1][cy1 - 1]
    
    print(total)