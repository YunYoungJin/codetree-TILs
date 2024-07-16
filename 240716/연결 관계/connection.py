n, m = map(int, input().split())

graph = [[] for _ in range(n)]

visited = [0] * n

for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)


def dfs(vertex, step):
    visited[vertex] = step

    for i in graph[vertex]:
        if not visited[i]:
            dfs(i, step + 1)

dfs(0, 0)

is_possible = False
for i in range(n):
    if visited[i] >= 4:
        is_possible = True
        break

if is_possible:
    print(1)
else:
    print(0)