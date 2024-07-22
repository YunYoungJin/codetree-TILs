import sys
import heapq

INT_MAX = sys.maxsize

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, v = map(int, input().split())
    graph[a - 1].append((b - 1, v))

dist = [INT_MAX] * n
dist[0] = 0
q = []
# dist, vertext
heapq.heappush(q, (0, 0))

while q:
    d, u = heapq.heappop(q)

    for vertex, length in graph[u]:
        tmp_dist = dist[u] + length
        if tmp_dist < dist[vertex]:
            dist[vertex] = tmp_dist
            heapq.heappush(q, (tmp_dist, vertex))

for i in range(1, n):
    if dist[i] == INT_MAX:
        print(-1)
    else:
        print(dist[i])