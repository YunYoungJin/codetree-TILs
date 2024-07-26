import sys
import heapq

INT_MAX = sys.maxsize

a, b, n = map(int, input().split())

def dijkstra(start, end, graph, N):
    # Initialize distances and priority queue
    distances = {i: (INT_MAX, INT_MAX) for i in range(1, 1001)}
    distances[start] = (0, 0)
    pq = [(0, 0, start)]  # (cost, time, node)

    while pq:
        current_cost, current_time, current_node = heapq.heappop(pq)

        if current_node == end:
            return current_cost, current_time

        for next_cost, next_time, neighbor in graph[current_node]:
            new_cost = current_cost + next_cost
            new_time = current_time + next_time

            if new_cost < distances[neighbor][0] or (new_cost == distances[neighbor][0] and new_time < distances[neighbor][1]):
                distances[neighbor] = (new_cost, new_time)
                heapq.heappush(pq, (new_cost, new_time, neighbor))

    return -1, -1

graph = {i: [] for i in range(1, 1001)}

for i in range(1, n + 1):
    cost, stop_cnt = map(int, input().split())
    stops = list(map(int, input().split()))

    for i in range(stop_cnt - 1):
        for j in range(i, stop_cnt):
            if i == j:
                continue
            time = j - i
            graph[stops[i]].append((cost, time, stops[j]))

min_cost, min_time = dijkstra(a, b, graph, n)

print(f"{min_cost} {min_time}")