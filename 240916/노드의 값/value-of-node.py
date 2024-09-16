import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

n = int(input())
values = [0] + list(map(int, input().split()))
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 필요한 연산 횟수
operations = 0

def dfs(node, parent):
    global operations
    # 현재 노드가 가져야 할 값과 실제 값의 차이
    balance = values[node] - 1

    # 자식 노드들 탐색
    for child in graph[node]:
        if child != parent:
            # 자식 노드에서의 값을 먼저 조정하고 그 결과를 받아옴
            child_balance = dfs(child, node)
            # 자식 노드의 불균형을 현재 노드로 전달
            balance += child_balance

    operations += abs(balance)

    return balance

# DFS 시작 (루트는 1번 노드로 가정)
dfs(1, -1)

print(operations)