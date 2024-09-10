import sys
from collections import deque
import heapq
INF = sys.maxsize

def bfs(start, n, graph):
    distances = [(-INF, INF)] * (n + 1)
    distances[start] = (0, 0)
    q = deque([(start, -1)])
    heap = []

    # BFS 수행
    while q:
        node, parent = q.popleft()
        for neighbor, weight in graph[node]:
            if neighbor == parent:
                continue
            
            edge_cnt = distances[node][0] + 1
            total_weight = distances[node][1] + weight
            distances[neighbor] = (edge_cnt, total_weight)
            heapq.heappush(heap, (-edge_cnt, total_weight, neighbor))
            q.append((neighbor, node))

    return heap[0][1], heap[0][2]


n, d = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

_, node_a = bfs(1, n, graph)

dist, _ = bfs(node_a, n, graph)

print((dist + d - 1) // d)