import sys
import heapq
import math
INF = sys.maxsize

n, m, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    i, j, l, c = map(int, input().split())
    graph[i].append((j, l, c))
    graph[j].append((i, l, c))


def calc(B, A):
    return B + (x / A)


pq = []
dist = [(INF, INF)] * (n + 1)  # (total length, minimum C value)
dist[1] = (0, INF)
heapq.heappush(pq, (0, INF, 1))

while pq:
    curr_length, curr_min_cost, node = heapq.heappop(pq)

    # Explore neighbors
    for neighbor, length, cost in graph[node]:
        new_length = curr_length + length
        new_min_cost = min(curr_min_cost, cost)
        
        # If a better route is found, update
        if calc(new_length, new_min_cost) < calc(dist[neighbor][0], dist[neighbor][1]):
            dist[neighbor] = (new_length, new_min_cost)
            heapq.heappush(pq, (new_length, new_min_cost, neighbor))
        elif calc(new_length, new_min_cost) == calc(dist[neighbor][0], dist[neighbor][1]):
            heapq.heappush(pq, (new_length, new_min_cost, neighbor))

# Final values for the path to N
final_length, final_min_cost = dist[n]

# Calculate the total time B + X / A
total_time = calc(final_length, final_min_cost)

print(math.floor(total_time))