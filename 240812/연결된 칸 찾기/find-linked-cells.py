from collections import deque

n = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

visited = [[False] * n for _ in range(n)]
q = deque()

def push(x, y):
    visited[x][y] = True
    q.append((x, y))

def bfs():
    cnt = 0
    while q:
        x, y = q.popleft()
        cnt += 1

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 1 and not visited[nx][ny]:
                push(nx, ny)
    
    return cnt

ans = []
for i in range(n):
    for j in range(n):
        if not visited[i][j] and grid[i][j] == 1:
            push(i, j)
            ans.append(bfs())

ans.sort()
print(len(ans))
for item in ans:
    print(item)