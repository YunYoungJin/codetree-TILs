from collections import deque

def bfs(start, n, graph):
    distances = [-1] * (n + 1)
    distances[start] = 0
    q = deque([start])
    parent = [-1] * (n + 1)

    while q:
        node = q.popleft()
        for neighbor in graph[node]:
            if distances[neighbor] == -1:  # 방문하지 않은 노드만 처리
                distances[neighbor] = distances[node] + 1
                parent[neighbor] = node
                q.append(neighbor)
    
    # 가장 먼 노드와 그 거리 반환
    max_distance = max(distances)
    farthest_node = distances.index(max_distance)

    return farthest_node, max_distance, parent


def find_tree_center(n, graph):
    # 임의의 노드에서 가장 먼 노드 A를 찾는다.
    node_a, _, _ = bfs(1, n, graph)
    
    # A에서 가장 먼 노드 B를 찾는다.
    node_b, diameter, parent = bfs(node_a, n, graph)

    # A에서 B까지의 경로 추적
    path = []
    current = node_b
    while current != -1:
        path.append(current)
        current = parent[current]
    
    # 중심 노드는 경로의 중간에 위치
    center = path[len(path) // 2]

    # Step 4: 트리의 중심에서 가장 먼 노드까지의 거리를 구한다.
    _, max_distance_from_center, _ = bfs(center, n, graph)

    return max_distance_from_center

n = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

print(find_tree_center(n, graph))