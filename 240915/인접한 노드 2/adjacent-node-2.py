import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

n = int(input())
score = [0] + list(map(int, input().split()))

dp = [[0] * 2 for _ in range(n + 1)]
graph = [[] for _ in range(n + 1)]
result_nodes = []

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(node, parent):
    dp[node][0] = 0 # node를 선택하지 않으면
    dp[node][1] = score[node] # node를 선택하면 

    for child in graph[node]:
        if child == parent:
            continue
        
        dfs(child, node)

        # node를 선택하지 않으면, 자식은 선택해도 안해도 된다.
        dp[node][0] += max(dp[child][0], dp[child][1])

        # node를 선택하면 자식은 선택할 수 없다.
        dp[node][1] += dp[child][0]


def trace(node, parent, is_selected):
    if is_selected:  # 노드가 선택되었다면
        result_nodes.append(node)
        for child in graph[node]:
            if child != parent:
                trace(child, node, 0)  # 자식 노드는 선택되지 않음
    else:  # 노드가 선택되지 않았다면
        for child in graph[node]:
            if child != parent:
                # 자식 노드가 선택되었는지 여부는 dp 값을 기준으로 결정
                if dp[child][0] < dp[child][1]:
                    trace(child, node, 1)
                else:
                    trace(child, node, 0)


# 임의의 노드를 루트로 정하고 dfs 시작
dfs(1, -1)

if dp[1][0] < dp[1][1]:
    trace(1, -1, 1)
else:
    trace(1, -1, 0)

print(max(dp[1][0], dp[1][1]))
result_nodes.sort()
print(*result_nodes)