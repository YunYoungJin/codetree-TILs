import sys
import heapq
input = sys.stdin.readline

INF = sys.maxsize

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, v = map(int, input().split())
    graph[a].append((b, v))
    graph[b].append((a, v))

def dijkstra(start):
    distance = [INF] * (n + 1)
    distance[start] = 0
    pq = [(0, start)]
    parents = [-1 for _ in range(n + 1)]

    while pq:
        current_dist, current_node = heapq.heappop(pq)
        
        if current_dist > distance[current_node]:
            continue
        
        for neighbor, weight in graph[current_node]:
            distance_via_node = current_dist + weight
            
            if distance_via_node < distance[neighbor]:
                distance[neighbor] = distance_via_node
                heapq.heappush(pq, (distance_via_node, neighbor))
                parents[neighbor] = current_node
            elif distance_via_node == distance[neighbor]:
                if parents[neighbor] == 1 or parents[neighbor] > current_node:
                    parents[neighbor] = current_node
    
    return distance, parents

for i in range(1, n):
    graph[i].sort()

dist, path = dijkstra(1)
visited = [False] * (n + 1)

x = n
while x != 1:
    x = path[x]
    visited[x] = True

for i in range(2, n):
    if visited[i]:
        graph[i].clear()

new_dist, _ = dijkstra(1)

print(new_dist[n] if new_dist[n] != INF else -1)