import heapq
import sys

INT_MAX = sys.maxsize
n, m = map(int, input().split())
graph = [
    [0] * (n + 1)
    for _ in range(n + 1)
]
pq = []
dist = [INT_MAX] * (n + 1)

# 그래프를 인접리스트로 표현합니다.
for i in range(1, m + 1):
    x, y, z = map(int, input().split())
    graph[x][y] = z
    graph[y][x] = z
a, b =map(int, input().split())

dist[b] = 0
heapq.heappush(pq, (0, b))

while pq:
    # 가장 거리가 가까운 정보를 받아온 뒤, 원소를 제거해줍니다.
    min_dist, min_index = heapq.heappop(pq)

    if min_dist != dist[min_index]:
        continue

    # 최솟값에 해당하는 정점에 연결된 간선들을 보며
    # 시작점으로부터의 최단거리 값을 갱신해줍니다.
    for j in range(1, n + 1):
        # 간선이 존재하지 않는 경우에는 넘어갑니다.
        if graph[min_index][j] == 0:
            continue

        if dist[j] > dist[min_index] + graph[min_index][j]:
            dist[j] = dist[min_index] + graph[min_index][j]
            heapq.heappush(pq, (dist[j], j))

print(dist[a])

x = a
print(x, end=' ')

while x != b:
    for i in range(1, n + 1):
        if graph[i][x] == 0:
            continue

        if dist[i] + graph[i][x] == dist[x]:
            x = i
            break
    
    print(x, end=' ')