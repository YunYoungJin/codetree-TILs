from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = set()

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

ans = 0
q = deque()

for i in range(1, n + 1):
    if i in visited:
        continue

    visited.add(i)
    q.append((i, -1))  # (현재 노드, 부모 노드)
    is_cycle = False

    # 연결요소 탐색
    while q:
        curr_node, parent = q.popleft()

        for neighbor in graph[curr_node]:
            if neighbor == parent:  # 부모 노드는 다시 방문하지 않음
                continue

            if neighbor in visited:  # 이미 방문한 노드가 나타나면 사이클이 있음
                is_cycle = True
            else:
                visited.add(neighbor)
                q.append((neighbor, curr_node))

    # 사이클이 없는 경우 카운트
    if not is_cycle:
        ans += 1

print(ans)