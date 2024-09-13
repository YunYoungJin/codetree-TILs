import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

n, r, q = map(int, input().split())
dp = [0] * (n + 1)

graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(node, parent):
    dp[node] = 1

    for child in graph[node]:
        if child == parent:
            continue
        
        dfs(child, node)

        dp[node] += dp[child]


dfs(r, -1)

for _ in range(q):
    u = int(input())
    print(dp[u])