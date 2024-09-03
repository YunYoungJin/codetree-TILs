import sys
import heapq

INT_MAX = sys.maxsize

n, m = map(int, input().split())
a, b, c = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    x, y, v = map(int, input().split())
    graph[x].append((y, v))
    graph[y].append((x, v))


def dijkstra(start):
    dist = [INT_MAX] * (n + 1)
    dist[start] = 0
    q = [(0, start)]

    while q:
        d, u = heapq.heappop(q)

        if d > dist[u]:
            continue

        for vertex, length in graph[u]:
            tmp_dist = dist[u] + length
            if tmp_dist < dist[vertex]:
                dist[vertex] = tmp_dist
                heapq.heappush(q, (tmp_dist, vertex))
    
    return dist

dist_a = dijkstra(a)
dist_b = dijkstra(b)
dist_c = dijkstra(c)

ans = 0
for i in range(1, n + 1):
    min_dist = min(dist_a[i], dist_b[i], dist_c[i])
    ans = max(ans, min_dist)

print(ans)