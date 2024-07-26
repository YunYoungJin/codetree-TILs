n, m = map(int, input().split())
graph = [
    list(map(int, input().split()))
    for _ in range(n)
]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][k] + graph[k][j] < graph[i][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

for _ in range(m):
    a, b = map(int, input().split())
    print(graph[a - 1][b - 1])