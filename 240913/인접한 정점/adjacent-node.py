import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

n = int(input())
score = [0] + list(map(int, input().split()))

dp = [[0] * 2 for _ in range(n + 1)]
graph = [[] for _ in range(n + 1)]

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


# 임의의 노드를 루트로 정하고 dfs 시작
dfs(n, -1)
print(max(dp[n][0], dp[n][1]))