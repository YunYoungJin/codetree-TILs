import sys

n = int(input())

cps = []

for _ in range(n):
    cps.append(tuple(map(int, input().split())))

min_dist = sys.maxsize

for i in range(1, n - 1):
    tmp = cps[:i] + cps[i + 1:]
    md = 0
    for j in range(len(tmp) - 1):
        md += abs(tmp[j][0] - tmp[j + 1][0]) + abs(tmp[j][1] - tmp[j + 1][1])
    min_dist = min(min_dist, md)
print(min_dist)