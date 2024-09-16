import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

n = int(input())

graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

values = [0]
for _ in range(n):
    values.append((int(input())))

k = int(input())
# dp[node][picked][total] : node를 picked 했을때, 안했을때 총 total 개의 노드를 색칠했을 때의 최대 값
dp = [[[0] * (k + 1) for _ in range(2)] for _ in range(n + 1)]

def dfs(node, parent):
    dp[node][1][1] = values[node]

    for child in graph[node]:
        if child != parent:
            dfs(child, node)

            # 업데이트를 위한 임시 배열
            temp_dp = [[0] * (k + 1) for _ in range(2)]

            # 현재 노드를 색칠하지 않는 경우
            for i in range(k + 1):
                temp_dp[0][i] = dp[node][0][i]
                for j in range(i + 1):
                    temp_dp[0][i] = max(temp_dp[0][i], dp[node][0][i - j] + dp[child][0][j])
                    temp_dp[0][i] = max(temp_dp[0][i], dp[node][0][i - j] + dp[child][1][j])

            # 현재 노드를 색칠하는 경우
            for i in range(1, k + 1):
                temp_dp[1][i] = dp[node][0][i - 1] + values[node]
                for j in range(i + 1):
                    temp_dp[1][i] = max(temp_dp[1][i], dp[node][1][i - j] + dp[child][0][j])

            # dp 업데이트
            for color in range(2):
                for i in range(k + 1):
                    dp[node][color][i] = temp_dp[color][i]


# 루트 1에서 DFS 시작
dfs(1, -1)
ans = 0

for t in range(k + 1):
    ans = max(ans, dp[1][0][t], dp[1][1][t])

print(ans)