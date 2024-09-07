from collections import deque

def bfs(start, end, n, graph):
    distances = [-1] * (n + 1)
    distances[start] = 0
    q = deque([start])
    
    # BFS 수행
    while q:
        node = q.popleft()

        if node == end:
            break
        
        for neighbor, weight in graph[node]:
            if distances[neighbor] == -1:  # 방문하지 않은 노드만 처리
                distances[neighbor] = distances[node] + weight
                q.append(neighbor)
    

    return distances[end]


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

for _ in range(m):
    a, b = map(int, input().split())
    print(bfs(a, b, n, graph))