import sys
import heapq
input = sys.stdin.readline

INF = sys.maxsize

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
edges = []

for _ in range(m):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))
    graph[b].append((a, w))
    edges.append((a, b, w))


def dijkstra(start):
    dist = [INF] * (n + 1)
    dist[start] = 0
    pq = [(0, start)]
    
    while pq:
        current_dist, current_node = heapq.heappop(pq)
        
        if current_dist > dist[current_node]:
            continue
        
        for neighbor, weight in graph[current_node]:
            distance = current_dist + weight
            if distance < dist[neighbor]:
                dist[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    return dist

dist_from_1 = dijkstra(1)
dist_from_n = dijkstra(n)
shortest_path = dist_from_1[n]

count = 0

for a, b, w in edges:
    if dist_from_1[a] + w + dist_from_n[b] == shortest_path or dist_from_1[b] + w + dist_from_n[a] == shortest_path:
        graph[a].remove((b, w))
        graph[b].remove((a, w))

        new_dist_from_1 = dijkstra(1)

        if new_dist_from_1[n] != shortest_path:
            count += 1
        
        graph[a].append((b, w))
        graph[b].append((a, w))      


print(count)