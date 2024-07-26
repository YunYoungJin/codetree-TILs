import sys

INT_MAX = sys.maxsize

n, m = map(int, input().split())

# dist 초기값을 전부 아주 큰 값으로 설정
dist = [
    [INT_MAX] * (n + 1)
    for _ in range(n + 1)
]

# 자기 자신은 0으로 설정
for i in range(1, n + 1):
    dist[i][i] = 0

for i in range(m):
    x, y, z = map(int, input().split())
    dist[x][y] = min(dist[x][y], z)


for k in range(1, n + 1): # 확실하게 거쳐갈 정점을 1번부터 N번까지 순서대로 정의
    for i in range(1, n + 1): # 고정된 k에 대해 모든 쌍 (i, j)를 탐색.
        for j in range(1, n + 1):
            # i에서 j로 가는 거리가 k를 경유해 가는 것이 더 좋다면
            # dist[i][j]값을 갱신
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

# 모든 쌍에 대한 최단거리 결과를 출력
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if dist[i][j] == INT_MAX:
            print(-1, end=" ")
        else:
            print(dist[i][j], end=" ")
    print()