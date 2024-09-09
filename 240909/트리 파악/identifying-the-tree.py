from collections import defaultdict, deque

def bfs_depth(n, graph):
    # BFS를 사용해 깊이 계산
    depth = [0] * (n + 1)
    visited = [False] * (n + 1)
    queue = deque([1])  # 루트 노드 1번
    visited[1] = True
    
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                depth[neighbor] = depth[node] + 1
                queue.append(neighbor)
    
    return depth

def can_a_win(n, edges):
    graph = defaultdict(list)
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)
    
    # 깊이 계산
    depth = bfs_depth(n, graph)
    
    # 리프 노드의 깊이 합 계산
    total_depth = 0
    for node in range(2, n + 1):
        if len(graph[node]) == 1:  # 리프 노드는 연결된 노드가 1개
            total_depth += depth[node]
    
    # 깊이 합이 홀수이면 A의 승리, 짝수이면 B의 승리
    return 1 if total_depth % 2 == 1 else 0


n = int(input())
edges = [
    tuple(map(int, input().split()))
    for _ in range(n - 1)
]

# A의 승리 여부 출력
print(can_a_win(n, edges))