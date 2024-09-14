import sys
sys.setrecursionlimit(30000)
input = sys.stdin.readline
INF = sys.maxsize

n = int(input())
values = [0]
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n + 1):
    values.append(int(input()))

max_sum = -INF

def dfs(node, parent):
    global max_sum
    
    left_max = 0
    right_max = 0
    
    for child in graph[node]:
        if child != parent:
            child_max = dfs(child, node)
            
            # Update left_max or right_max based
            if child_max > left_max:
                right_max = left_max
                left_max = child_max
            elif child_max > right_max:
                right_max = child_max
    
    # Calculate the maximum path sum including the current node
    max_sum = max(max_sum, values[node] + left_max + right_max)
    
    # Return the maximum path sum for the current node to parent
    return values[node] + left_max

# DFS 시작 (루트 노드 1부터)
dfs(1, -1)

# 최대 경로 합 출력
print(max_sum)