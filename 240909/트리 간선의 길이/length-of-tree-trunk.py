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

    return farthest_node, max_distance


n = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

# 임의의 노드에서 가장 먼 노드 찾기
farthest_node, _ = bfs(1, n, graph)

# 가장 먼 노드에서 다시 가장 먼 노드를 찾아 정답 계산
_, ans = bfs(farthest_node, n, graph)

print(ans)