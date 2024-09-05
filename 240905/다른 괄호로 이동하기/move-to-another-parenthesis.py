import sys
import heapq

INF = sys.maxsize

n, a, b = map(int, input().split())
grid = [
    list(input())
    for _ in range(n)
]

dxdys = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def in_range(x, y):
    return (0 <= x and x < n) and (0 <= y and y < n)


def dijkstra(sx, sy):
    dist = [[INF] * n for _ in range(n)]
    pq = []

    dist[sx][sy] = 0
    heapq.heappush(pq, (0, sx, sy))

    while pq:
        curr_dist, x, y = heapq.heappop(pq)

        if curr_dist > dist[x][y]:
            continue
        
        for dx, dy in dxdys:
            nx, ny = x + dx, y + dy

            if in_range(nx, ny):
                if grid[x][y] == grid[nx][ny]:
                    cost = a
                else:
                    cost = b
                
                new_dist = curr_dist + cost
            
                if new_dist < dist[nx][ny]:
                    dist[nx][ny] = new_dist
                    heapq.heappush(pq, (new_dist, nx, ny))
    
    max_dist = 0
    for i in range(n):
        for j in range(n):
            if dist[i][j] < INF:
                max_dist = max(max_dist, dist[i][j])
    
    return max_dist

ans = 0

for i in range(n):
    for j in range(n):
        ans = max(ans, dijkstra(i, j))

print(ans)