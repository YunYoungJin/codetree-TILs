import sys
INF = sys.maxsize


n = int(input())
placement_costs = [
    int(input())
    for _ in range(n)
]
connection_cost = [
    list(map(int, input().split()))
    for _ in range(n)
]

ans = sum(placement_costs)

for start in range(n):
    dist = [INF] * n
    dist[start] = placement_costs[start]
    visited = [False] * n
    tmp_cost = 0

    for i in range(n):
        min_index = -1
        for j in range(n):
            if visited[j]:
                continue
            
            if min_index == -1 or dist[min_index] > dist[j]:
                min_index = j
        
        visited[min_index] = True

        tmp_cost += dist[min_index]

        for j in range(n):
            if connection_cost[min_index][j] == 0:
                continue
            
            dist[j] = min(dist[j], placement_costs[j], connection_cost[min_index][j])

    ans = min(ans, tmp_cost)

print(ans)