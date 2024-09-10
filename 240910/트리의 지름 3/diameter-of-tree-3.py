from collections import deque

def bfs(start, n, graph):
    distances = [-1] * (n + 1)
    distances[start] = 0
    q = deque([start])
    
    # BFS 수행
    while q:
        node = q.popleft()
        for neighbor, weight in graph[node]:
            if distances[neighbor] == -1:  # 방문하지 않은 노드만 처리
                distances[neighbor] = distances[node] + weight
                q.append(neighbor)
    
    # 가장 먼 노드와 그 거리 반환
    max_distance = max(distances)
    farthest_node = distances.index(max_distance)

    return farthest_node, distances


n = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

# 지름의 한쪽 끝 찾기
a, dist_from_1 = bfs(1, n, graph)

# 지름의 나머지 한쪽 찾기
b, dist_from_a = bfs(a, n, graph)

_, dist_from_b = bfs(b, n, graph)

dist_from_a[b] = -1
dist_from_b[a] = -1

ans = max(max(dist_from_a), max(dist_from_b))
print(ans)