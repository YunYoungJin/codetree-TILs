n, q = map(int, input().split())
points = list(map(int, input().split()))
points.sort()
qureies = [
    tuple(map(int, input().split()))
    for _ in range(q)
]

largest_x = points[-1]
xs = [0] * (1000001)
prefix_cnt = [0] * (1000002)

for x in points:
    xs[x] = 1

for i in range(1, 1000002):
    prefix_cnt[i] = prefix_cnt[i - 1] + xs[i - 1]

for a, b in qureies:
    print(prefix_cnt[b + 1] - prefix_cnt[a])