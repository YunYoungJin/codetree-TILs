import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
INF = sys.maxsize

n = int(input())
parent = [-1] * (n + 1)
children = [[] for _ in range(n + 1)]
depth = [INF] * (n + 1)

for _ in range(n - 1):
    p, c = map(int, input().split())
    parent[c] = p
    children[p].append(c)

a, b = map(int, input().split())

parent[0] = INF
root = parent.index(-1)
depth[root] = 0

def dfs(node):
    # 노드 x의 자식들을 살펴봅니다.
    for child in children[node]:
        # depth값을 갱신해주며
        # 재귀적으로 탐색합니다.
        depth[child] = depth[node] + 1
        dfs(child)

dfs(root)

while depth[a] != depth[b]:
    if depth[a] > depth[b]:
        a = parent[a]
    else:
        b = parent[b]

while a != b:
    a = parent[a]
    b = parent[b]

print(a)