n = int(input())
points = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

ans = 2000001

for i in range(n):
    for j in range(i + 1, n):
        x1, y1 = points[i]
        x2, y2 = points[j]

        dist = (x2 - x1) ** 2 + (y2 - y1) ** 2
        ans = min(ans, dist)

print(ans)