import sys
import heapq
from collections import deque
input = sys.stdin.readline

n, m, t = map(int, input().split())
t = min(t, 2 * n)

beads = deque()

for i in range(1, m + 1):
    r, c, d, w = input().split()
    r, c, w = int(r) - 1, int(c) - 1, int(w)
    beads.append((i, r, c, d, w))

direction_map = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
opposite_direction = {'U': 'D', 'D': 'U', 'L': 'R', 'R': 'L'}
max_weight = -sys.maxsize

for _ in range(t):
    cnt = len(beads)
    moved_map = [[[] for _ in range(n)] for _ in range(n)]
    positions = set()

    for _ in range(cnt):
        idx, r, c, d, w = beads.popleft()

        dr, dc = direction_map[d]
        new_r, new_c = r + dr, c + dc

        if not (0 <= new_r < n and 0 <= new_c < n):
            d = opposite_direction[d]
            new_r, new_c = r, c

        heapq.heappush(moved_map[new_r][new_c], (-idx, new_r, new_c, d, w))
        positions.add((new_r, new_c))

    for i, j in positions:
        idx, r, c, d, w = moved_map[i][j][0]
        cnt = len(moved_map[i][j])
        if cnt >= 2:
            for k in range(cnt - 1, 0, -1):
                w += moved_map[i][j][k][4]
        max_weight = max(max_weight, w)
        beads.append((-idx, r, c, d, w))

print(len(beads), max_weight)