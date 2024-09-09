from collections import defaultdict, deque

n, k = map(int, input().split())
arr = list(map(int, input().split()))

graph = defaultdict(list)
parent = dict()
root = arr[0]
parent[root] = None
current_parent = root
parent_candidates = deque()


for i in range(1, n):
    # 연속된 수가 아닌 경우 새로운 집합으로 분리
    graph[current_parent].append(arr[i])
    parent[arr[i]] = current_parent
    parent_candidates.append(arr[i])
    if i < n - 1 and arr[i] + 1 != arr[i + 1]:
        current_parent = parent_candidates.popleft()


# k의 부모를 확인
# 부모가 루트거나, 없으면 사촌은 없음
if parent[k] is root or parent[k] is None:
    print(0)
else:
    k_parent = parent[k]

    # 부모의 형제 노드(즉, 사촌의 부모)를 찾음
    k_grandparent = parent[k_parent]

    # 사촌 노드 수 계산
    cousin_count = 0
    for sibling_parent in graph[k_grandparent]:
        if sibling_parent != k_parent:
            cousin_count += len(graph[sibling_parent])
    
    print(cousin_count)