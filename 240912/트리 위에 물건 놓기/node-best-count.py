import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

n = int(input())
dp = [[0] * 2 for _ in range(n + 1)]

graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(node, parent):
    dp[node][0] = 0 # node에 물건을 놓지 않으면
    dp[node][1] = 1 # node에 물건을 놓으면

    for child in graph[node]:
        if child == parent:
            continue
        
        dfs(child, node)

        # node에 물건을 놓지 않으면, 자식에는 반드시 물건을 놓아야 함
        dp[node][0] += dp[child][1]

        # node에 물건을 놓으면, 자식에는 놓아도 되고, 안 놓아도 됨
        dp[node][1] += min(dp[child][0], dp[child][1])


# 임의의 노드를 루트로 정하고 dfs 시작
dfs(n, -1)
print(min(dp[n][0], dp[n][1]))