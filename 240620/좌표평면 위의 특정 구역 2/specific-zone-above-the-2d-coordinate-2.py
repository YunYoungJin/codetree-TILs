import sys

n = int(input())
points = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

min_area = sys.maxsize

for i in range(n):
    xs = []
    ys = []
    for j in range(n):
        if j == i:
            continue

        x, y = points[j]
        xs.append(x)
        ys.append(y)

    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)

    area = (max_x - min_x) * (max_y - min_y)
    min_area = min(min_area, area)

print(min_area)