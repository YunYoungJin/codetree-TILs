n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [False] * (n + 1)

def dfs(vertex):
    for curr_v in graph[vertex]:
        if not visited[curr_v]:
            visited[curr_v] = True
            dfs(curr_v)

root_vertex = 1
visited[root_vertex] = True

dfs(root_vertex)
print(visited.count(True) - 1)