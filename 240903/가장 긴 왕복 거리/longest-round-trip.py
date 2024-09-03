import sys
import heapq
input = sys.stdin.readline

INF = sys.maxsize
n, m, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
reverse_graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, v = map(int, input().split())
    graph[a].append((b, v))
    reverse_graph[b].append((a, v))

def dijkstra(start, graph):
    distance = [INF] * (n + 1)
    distance[start] = 0
    pq = [(0, start)]
    
    while pq:
        current_dist, current_node = heapq.heappop(pq)
        
        if current_dist > distance[current_node]:
            continue
        
        for neighbor, weight in graph[current_node]:
            distance_via_node = current_dist + weight
            
            if distance_via_node < distance[neighbor]:
                distance[neighbor] = distance_via_node
                heapq.heappush(pq, (distance_via_node, neighbor))
    
    return distance

dist = dijkstra(x, graph)
reverse_dist = dijkstra(x, reverse_graph)

ans = 0
for i in range(1, n + 1):
    rtt = dist[i] + reverse_dist[i]
    ans = max(ans, rtt)

print(ans)