import sys
INF = sys.maxsize

n, m, p, q = map(int, input().split())

dist = [
    [INF] * (n + 1)
    for _ in range(n + 1)
]
queries = []

for i in range(1, n + 1):
    dist[i][i] = 0

for _ in range(m):
    x, y, z = map(int, input().split())
    dist[x][y] = z

for _ in range(q):
    a, b = map(int, input().split())
    queries.append((a, b))

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

cnt = 0
cost = 0

for a, b in queries:
    tmp = INF
    for k in range(1, p + 1):
        if dist[a][k] == INF or dist[k][b] == INF:
            continue
        tmp = min(tmp, dist[a][k] + dist[k][b])

    if tmp != INF:
        cnt += 1
        cost += tmp

print(cnt)
print(cost)