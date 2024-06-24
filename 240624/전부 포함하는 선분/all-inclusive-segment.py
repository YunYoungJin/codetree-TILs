n = int(input())

segments = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

segments.sort(key = lambda x : x[0])

ans = 100
min_x1, max_x2 = 101, 0
for segment in segments[1:]:
    x1, x2 = segment
    min_x1 = min(min_x1, x1)
    max_x2 = max(max_x2, x2)

ans = min(ans, max_x2 - min_x1)

segments.sort(key = lambda x : -x[1])
min_x1, max_x2 = 101, 0
for segment in segments[1:]:
    x1, x2 = segment
    min_x1 = min(min_x1, x1)
    max_x2 = max(max_x2, x2)

ans = min(ans, max_x2 - min_x1)

print(ans)