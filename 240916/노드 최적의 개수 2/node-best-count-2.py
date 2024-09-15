import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

initial_items = list(map(int, input().split()))
selected = [False] * (n + 1)

for node in initial_items:
    selected[node] = True

extra_items = 0

def dfs(node, parent):
    global extra_items

    # 해당 노드에 물건을 놓아야 하는지 여부
    needs_item = False

    for child in graph[node]:
        if child == parent:
            continue
        
        # 자식 노드 탐색
        if dfs(child, node):
            needs_item = True

    # 현재 노드가 자식 노드에 의해 커버되지 않고 물건도 없다면, 현재 노드에 물건을 놓음
    if needs_item and not selected[node]:
        selected[node] = True
        extra_items += 1

    # 현재 노드에 물건이 있거나, 자식노드에 의해 커버되었다면 
    return not selected[node]

# 임의의 노드를 루트로 정하고 dfs 시작
dfs(1, -1)
print(extra_items)