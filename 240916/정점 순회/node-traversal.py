import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

n, s, d = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)
dp = [-1] * (n + 1)  # 

# 서브트리에서 가장 멀리 있는 리프노드까지의 거리

def calc_depth(node, parent):
    max_depth = 0

    for child in graph[node]:
        if child != parent:
            child_depth = calc_depth(child, node)
            max_depth = max(max_depth, child_depth + 1)
    
    dp[node] = max_depth

    return max_depth

calc_depth(s, -1)

# DFS를 통해 이동해야 할 최소 거리를 계산
def find_min_distance(node, parent):
    total_distance = 0
    for child in graph[node]:
        if child != parent:
            if dp[child] >= d:
                total_distance += find_min_distance(child, node) + 1

    return total_distance

# 최종 이동 거리 계산
result = find_min_distance(s, -1)
print(2 * result)