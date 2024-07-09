from sortedcontainers import SortedSet

n, m = map(int, input().split())
points = [
    tuple(map(int, input().split()))
    for _ in range(n)
]
s = SortedSet(points)

for _ in range(m):
    k = int(input())

    idx = s.bisect_left((k, 1))

    if idx == len(s):
        print(-1, -1)
    else:
        print(s[idx][0], s[idx][1])
        s.remove(s[idx])