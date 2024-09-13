import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
parent = list(map(int, input().split()))
dp = [0] * (n + 1)

graph = [[] for _ in range(n + 1)]

# 연산의 편의를 위해 부모 노드 기준으로, 자식 노드들만 저장
for idx, p_node in enumerate(parent):
    if p_node != -1:
        graph[p_node].append(idx + 1)

# BFS 방식으로 점수 계산
def calc():
    q = deque([1])

    while q:
        node = q.popleft()

        for child in graph[node]:
            dp[child] += dp[node]
            q.append(child)

# 초기 점수 등록
for _ in range(m):
    i, w = map(int, input().split())
    dp[i] += w

calc()
print(*dp[1:])