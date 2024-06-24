n = int(input())

points = []
for i in range(1, n + 1):
    x, y = map(int, input().split())
    points.append((i, x, y))

points.sort(key = lambda x : (abs(x[1]) + abs(x[2]), x[0]))

for num, _, _ in points:
    print(num)