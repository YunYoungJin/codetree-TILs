import sys
from collections import deque, defaultdict
input = sys.stdin.readline


# 입력 처리 및 시뮬레이션
t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    beads = deque()
    cnt_map = [[0] * n for _ in range(n)]
    for _ in range(m):
        x, y, d = input().split()
        x, y = int(x) - 1, int(y) - 1
        beads.append((x, y, d))
        cnt_map[x][y] = 1

    direction_map = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
    opposite_direction = {'U': 'D', 'D': 'U', 'L': 'R', 'R': 'L'}

    for _ in range(2 * n):
        cnt = len(beads)

        for _ in range(cnt):
            curr_x, curr_y, d = beads.popleft()

            dx, dy = direction_map[d]
            new_x, new_y = curr_x + dx, curr_y + dy

            if not (0 <= new_x < n and 0 <= new_y < n):
                # 벽에 부딪히면 방향 반전
                d = opposite_direction[d]
                new_x, new_y = curr_x, curr_y
            else:
                cnt_map[curr_x][curr_y] -= 1
                cnt_map[new_x][new_y] += 1

            beads.append((new_x, new_y, d))

        collision = set()

        for _ in range(cnt):
            x, y, d = beads.popleft()
            if cnt_map[x][y] >= 2:
                collision.add((x, y))
            else:
                beads.append((x, y, d))
        
        if collision:
            for i, j in collision:
                cnt_map[i][j] = 0

    print(len(beads))