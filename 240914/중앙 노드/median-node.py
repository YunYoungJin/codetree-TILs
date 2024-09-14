import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

n, r = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dp = [0] * (n + 1)

def dfs(node, parent):
    dp[node] = 1

    for child in graph[node]:
        if child == parent:
            continue
        
        dfs(child, node)

        dp[node] += dp[child]


def find_central(node, parent):
    global central_node

    # 루트일 경우, 자식이 2개 이상인지 확인
    if parent == -1 and len(graph[node]) >= 2:
        central_node = node
        return
    # 루트 노드가 아니면, 부모 노드 포함 연결 노드가 3개 이상인지 확인
    elif parent != -1 and len(graph[node]) >= 3:
        central_node = node
        return
    # 리프노드까지 중앙 노드를 못찾으면 리프노드가 중앙노드
    elif len(graph[node]) == 1 and graph[node][0] == parent:
        central_node = node
        return
    
    # 루트가 아니면 
    for child in graph[node]:
        if child != parent:
            find_central(child, node)



central_node = r
find_central(r, -1)
dfs(central_node, -1)

max_size = 0
min_size = sys.maxsize

for child in graph[central_node]:
    max_size = max(max_size, dp[child])
    min_size = min(min_size, dp[child])

print(max_size - min_size)