n, m = map(int, input().split())
graph = [[0] * n for _ in range(n)]

for _ in range(m):
    a, b = map(lambda x: int(x) - 1, input().split())
    graph[a][b] = 1

for i in range(n):
    graph[i][i] = 1

# 거쳐갈 정점 k를 선택한 후
for k in range(n):
    for i in range(n): # 고정된 k에 대해 모든 쌍 (i, j)를 체크
        for j in range(n):
            # i -> k, k -> j로 가능 길이 있다면
            # i -> j도 가능하다는 뜻입니다.
            if graph[i][k] and graph[k][j]:
                graph[i][j] = 1


for i in range(n):
    cnt = 0
    for j in range(n):
        if graph[i][j] == 0 and graph[j][i] == 0:
            cnt += 1
    print(cnt)