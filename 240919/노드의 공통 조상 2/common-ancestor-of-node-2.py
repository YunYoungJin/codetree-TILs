import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

n = int(input())

# 트리 초기화
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

q = int(input())
queries = [
    tuple(map(int, input().split()))
    for _ in range(q)
]

# 각 노드의 깊이와 부모를 저장할 배열
depth = [0] * (n + 1)
parent = [[-1] * 17 for _ in range(n + 1)]  # 17 = ceil(log2(50000))

# DFS를 사용하여 깊이와 부모를 설정
def dfs(node, par):
    parent[node][0] = par
    for child in graph[node]:
        if child == par:
            continue
        depth[child] = depth[node] + 1
        dfs(child, node)

# 1번 노드를 루트로 DFS 시작
dfs(1, -1)

# 희소 테이블 구성: 2^k 번째 부모를 채움
for k in range(1, 17):
    for i in range(1, n + 1):
        if parent[i][k - 1] != -1:
            parent[i][k] = parent[parent[i][k - 1]][k - 1]

# 두 노드의 최소 공통 조상(LCA) 찾기 함수
def lca(u, v):
    # 항상 u의 깊이가 v보다 깊도록 설정
    if depth[u] < depth[v]:
        u, v = v, u

    # 깊이를 맞추기
    for i in range(16, -1, -1):
        if depth[u] - (1 << i) >= depth[v]:
            u = parent[u][i]

    # 깊이가 맞춰졌을 때 두 노드가 같다면 그것이 LCA
    if u == v:
        return u

    # 두 노드를 같은 레벨로 올리면서 조상 찾기
    for i in range(16, -1, -1):
        if parent[u][i] != parent[v][i]:
            u = parent[u][i]
            v = parent[v][i]

    # LCA는 두 노드의 바로 위 부모
    return parent[u][0]

for u, v in queries:
    print(lca(u, v))