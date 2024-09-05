import sys
import heapq
input = sys.stdin.readline

INF = sys.maxsize

n, m = map(int, input().split())
graph_a = [[] for _ in range(n + 1)]
graph_b = [[] for _ in range(n + 1)]
reverse_graph_a = [[] for _ in range(n + 1)]
reverse_graph_b = [[] for _ in range(n + 1)]

for _ in range(m):
    v1, v2, w1, w2 = map(int, input().split())
    graph_a[v1].append((v2, w1))
    graph_b[v1].append((v2, w2))
    reverse_graph_a[v2].append((v1, w1))
    reverse_graph_b[v2].append((v1, w2))

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

dist_a_from_n = dijkstra(n, reverse_graph_a)
dist_b_from_n = dijkstra(n, reverse_graph_b)

def modified_dijkstra(a_dist, b_dist, a_graph, b_graph):
    warning = [INF] * (n + 1)
    warning[1] = 0
    pq = [(0, 1)]

    while pq:
        min_warning, curr_node = heapq.heappop(pq)

        if min_warning > warning[curr_node]:
            continue

        for j in range(len(a_graph[curr_node])):
            target_node, a_cost = a_graph[curr_node][j]
            _, b_cost = b_graph[curr_node][j]

            warn_cnt = 0
            if a_dist[target_node] + a_cost != a_dist[curr_node]:
                warn_cnt += 1
            if b_dist[target_node] + b_cost != b_dist[curr_node]:
                warn_cnt += 1

            new_warning = warning[curr_node] + warn_cnt
            if warning[target_node] > new_warning:
                warning[target_node] = new_warning
                heapq.heappush(pq, (new_warning, target_node))
    
    return warning

warning_count = modified_dijkstra(dist_a_from_n, dist_b_from_n, graph_a, graph_b)

print(warning_count[n])