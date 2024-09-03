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

def dijkstra(start, graph):
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

def find_used_edges(parents, end_node):
    queue = [end_node]
    used_edges = set()

    while queue:
        current = queue.pop()
        if (current, parents[current]) not in used_edges:
            used_edges.add((current, parents[current]))
            queue.append(parents[current])

    return used_edges

dist_a, parents_a = dijkstra(1, graph)
used_edges = find_used_edges(parents_a, n)

new_graph = [[] for _ in range(n + 1)]
for u in range(1, n + 1):
    for v, w in graph[u]:
        if (u, v) not in used_edges and (v, u) not in used_edges:
            new_graph[u].append((v, w))

new_dist, _ = dijkstra(1, new_graph)
print(new_dist[n] if new_dist[n] != INF else -1)