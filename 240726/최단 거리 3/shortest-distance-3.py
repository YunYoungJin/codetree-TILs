import sys
import heapq

INT_MAX = sys.maxsize
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    x, y, v = map(int, input().split())
    if (y, v) not in graph[x]:
        graph[x].append((y, v))
    if (x, v) not in graph[y]:
        graph[y].append((x, v))

a, b = map(int, input().split())

dist = [INT_MAX] * (n + 1)
pq = []

dist[a] = 0
heapq.heappush(pq, (0, a))

while pq:
    min_dist, curr_vertex = heapq.heappop(pq)

    if min_dist != dist[curr_vertex]:
        continue
    
    for traget_vertex, target_dist in graph[curr_vertex]:
        new_dist = min_dist + target_dist
        if dist[traget_vertex] > new_dist:
            dist[traget_vertex] = new_dist
            heapq.heappush(pq, (new_dist, traget_vertex))

print(dist[b])