import sys
from collections import deque

INT_MAX = sys.maxsize
n = int(input())
r1, c1, r2, c2 = map(int, input().split())
r1, c1, r2, c2 = r1 - 1, c1 - 1, r2 - 1, c2 -1

q = deque()
visited = [[0] * n for _ in range(n)]
step = [[INT_MAX] * n for _ in range(n)]

# 8 방향
dxs = [-2, -1, 1, 2, 2, 1, -1, -2]
dys = [1, 2, 2, 1, -1, -2, -2, -1]


def in_range(x, y):
    return (0 <= x and x < n) and (0 <= y and y < n)


def can_go(nx, ny):
    if not in_range(nx, ny):
        return False

    if visited[nx][ny]:
        return False

    return True


def push(nx, ny, s):
    visited[nx][ny] = 1
    step[nx][ny] = min(step[nx][ny], s)
    q.append((nx, ny))


def bfs():
    while len(q) != 0:
        curr_x, curr_y = q.popleft()
        
        for dx, dy in zip(dxs, dys):
            nx, ny = curr_x + dx, curr_y + dy

            if can_go(nx, ny):
                push(nx, ny, step[curr_x][curr_y] + 1)

push(r1, c1, 0)
bfs()

if step[r2][c2] == INT_MAX:
    print(-1)
else:
    print(step[r2][c2])