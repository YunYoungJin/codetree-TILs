import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

n, s, d = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(node, parent):
    max_depth = 0
    total_distance = 0

    for child in graph[node]:
        if child != parent:
            child_depth, child_distance = dfs(child, node)
            max_depth = max(max_depth, child_depth + 1)
            # dp 배열을 사용하지 않고 필요할 때만 거리 계산
            if child_depth >= d:
                total_distance += child_distance + 1

    return max_depth, total_distance

# 최종 이동 거리 계산
_, result = dfs(s, -1)

print(2 * result)