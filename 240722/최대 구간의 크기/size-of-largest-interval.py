n = int(input())
segments = []

for _ in range(n):
    a, b = map(int, input().split())
    segments.append((a, 1))
    segments.append((b, -1))

segments.sort()

ans = 0
tmp_sum = 0
start = None

for x, v in segments:
    tmp_sum += v

    if tmp_sum > 0:
        if start is None:
            start = x
    
    if tmp_sum == 0:
        ans = max(ans, x - start)
        start = None

print(ans)