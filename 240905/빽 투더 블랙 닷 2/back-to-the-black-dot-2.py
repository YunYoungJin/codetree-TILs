import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize

n, m = map(int, input().split())
r1, r2 = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    i, j, d = map(int, input().split())
    graph[i].append((j, d))
    graph[j].append((i, d))

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

red_dot1_dist = dijkstra(r1)
red_dot2_dist = dijkstra(r2)
red_dot_cost = red_dot1_dist[r2]

ans = INF

for i in range(1, n + 1):
    if i == r1 or i == r2:
        continue
    
    ans = min(ans, red_dot1_dist[i] + red_dot_cost + red_dot2_dist[i])

print(ans if ans != INF else -1)