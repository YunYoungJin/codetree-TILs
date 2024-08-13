from collections import deque

n, m = map(int, input().split())
after_move = [[deque([int(num)]) for num in input().split()] for _ in range(n)]
grid = [[0] * n for _ in range(n)]

queries = list(map(int, input().split()))
number_pos = {}

for i in range(n):
    for j in range(n):
        grid[i][j] = after_move[i][j][0]
        number_pos[grid[i][j]] = (i, j)

for num in queries:
    x, y = number_pos[num]
    max_value = 0
    best_pos = (x, y)

    for dx, dy in [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n:
            if grid[nx][ny] > max_value:
                max_value = grid[nx][ny]
                best_pos = (nx, ny)

    if max_value == 0:
        continue

    nx, ny = best_pos
    tmp = []
    target = after_move[x][y].popleft()

    while target != num:
        tmp.append(target)
        target = after_move[x][y].popleft()
    tmp.append(target)

    if len(after_move[x][y]) == 0:
        grid[x][y] = 0
    else:
        grid[x][y] = max(after_move[x][y])

    while len(tmp) != 0:
        tmp_num = tmp.pop()
        after_move[nx][ny].appendleft(tmp_num)
        number_pos[tmp_num] = (nx, ny)
    grid[nx][ny] = max(after_move[nx][ny])

for i in range(n):
    for j in range(n):
        if after_move[i][j]:
            print(*after_move[i][j])
        else:
            print('None')