from collections import deque, defaultdict

m = int(input())
edges = [tuple(map(int, input().split())) for _ in range(m)]

def is_tree(m, edges):
    # 그래프 초기화
    in_degree = defaultdict(int)
    graph = defaultdict(list)
    nodes = set()
    
    # 그래프 및 진입 차수 설정
    for a, b in edges:
        graph[a].append(b)
        in_degree[b] += 1
        nodes.add(a)
        nodes.add(b)
    
    # 루트 노드 찾기: 진입 차수가 0인 노드
    root_candidates = [node for node in nodes if in_degree[node] == 0]
    
    # 루트가 하나가 아닌 경우 트리가 아님
    if len(root_candidates) != 1:
        return 0
    
    # 루트 노드 설정
    root = root_candidates[0]
    
    # 모든 노드를 방문했는지 확인하기 위한 집합
    visited = set()
    queue = deque([root])
    
    # BFS로 노드 방문
    while queue:
        node = queue.popleft()
        
        # 이미 방문한 노드라면 싸이클이 존재함
        if node in visited:
            return 0
        
        visited.add(node)
        
        for neighbor in graph[node]:
            queue.append(neighbor)
    
    # 모든 노드를 방문하지 않았다면 트리가 아님
    if len(visited) != len(nodes):
        return 0
    
    # 모든 조건을 만족하면 트리
    return 1


print(is_tree(m, edges))