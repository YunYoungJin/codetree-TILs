import heapq
import sys

INT_MAX = sys.maxsize
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
pq = []

dist = [INT_MAX] * (n + 1)
dist[0] = 0

# 그래프를 인접리스트로 표현합니다.
for i in range(1, m + 1):
    x, y, z = map(int, input().split())
    graph[y].append((x, z))

dist[n] = 0
heapq.heappush(pq, (0, n))

while pq:
    # 가장 거리가 가까운 정보를 받아온 뒤, 원소를 제거해줍니다.
    min_dist, min_index = heapq.heappop(pq)

    if min_dist != dist[min_index]:
        continue

    for target_index, target_dist in graph[min_index]:
        # 현재 위치에서 연결된 간선으로 가는 것이 더 작다면
        new_dist = dist[min_index] + target_dist
        if dist[target_index] > new_dist:
            # 값을 갱신해주고, 우선순위 큐에 해당 정보를 넣어줍니다.
            dist[target_index] = new_dist
            heapq.heappush(pq, (new_dist, target_index))

print(max(dist))