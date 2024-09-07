import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

# DFS를 통해 부모 노드를 찾는 함수
def dfs(node, parent):
    for neighbor in graph[node]:
        if parent_nodes[neighbor] == 0:  # 부모가 아직 설정되지 않은 경우
            parent_nodes[neighbor] = node  # 부모 설정
            dfs(neighbor, node)  # 자식 노드로 DFS 진행

n = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

parent_nodes = [0] * (n + 1)

# 루트 노드부터 DFS 시작
dfs(1, 0)

# 2번 노드부터 n번 노드까지 부모 노드 출력
for i in range(2, n + 1):
    print(parent_nodes[i])