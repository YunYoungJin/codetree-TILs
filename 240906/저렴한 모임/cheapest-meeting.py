import sys
INF = sys.maxsize

n, m = map(int, input().split())
v1, v2, e = map(int, input().split())

dist = [
    [INF] * (n + 1)
    for _ in range(n + 1)
]

for i in range(1, n + 1):
    dist[i][i] = 0

for i in range(m):
    x, y, z = map(int, input().split())
    dist[x][y] = z
    dist[y][x] = z


for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

ans = INF

for k in range(1, n + 1):
    if dist[v1][k] == INF or dist[v2][k] == INF or dist[k][e] == INF:
        continue
    ans = min(ans, dist[v1][k] + dist[v2][k] + dist[k][e])

print(ans if ans != INF else -1)