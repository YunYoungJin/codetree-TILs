import sys
import heapq
input = sys.stdin.readline

INF = sys.maxsize

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
edges = []

for _ in range(m):
    i, j, d = map(int, input().split())
    graph[i].append((j, d))
    graph[j].append((i, d))
    edges.append((i, j, d))


def dijkstra(start, graph):
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

dist_from_1 = dijkstra(1, graph)
dist_from_n = dijkstra(n, graph)
shortest_path = dist_from_1[n]
longest_path = 0

# 최단 경로가 아닌 간선은 2배를 해도 최단거리에 영향을 미치지 않음
for a, b, w in edges:
    if dist_from_1[a] + w + dist_from_n[b] == shortest_path or dist_from_1[b] + w + dist_from_n[a] == shortest_path:
        graph[a].remove((b, w))
        graph[b].remove((a, w))
        graph[a].append((b, 2 * w))
        graph[b].append((a, 2 * w))

        new_dist_from_1 = dijkstra(1, graph)

        longest_path = max(longest_path, new_dist_from_1[n])
        
        graph[a].remove((b, 2 * w))
        graph[b].remove((a, 2 * w))
        graph[a].append((b, w))
        graph[b].append((a, w))

print(abs(longest_path - shortest_path))