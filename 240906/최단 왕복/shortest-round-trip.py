import sys

INF = sys.maxsize

n, m = map(int, input().split())

dist = [
    [INF] * (n + 1)
    for _ in range(n + 1)
]

for i in range(1, n + 1):
    dist[i][i] = 0

for i in range(m):
    x, y, z = map(int, input().split())
    dist[x][y] = min(dist[x][y], z)


for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            # i에서 j로 가는 거리가 k를 경유해 가는 것이 더 좋다면
            # dist[i][j]값을 갱신
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

ans = INF
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            continue
        ans = min(ans, dist[i][j] + dist[j][i])

print(ans)