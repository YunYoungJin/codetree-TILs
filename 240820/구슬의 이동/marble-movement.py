import sys
import heapq
from collections import deque
input = sys.stdin.readline

n, m, t, k = map(int, input().split())
t = min(t, 2 * n)

beads = deque()

for i in range(1, m + 1):
    r, c, d, v = input().split()
    r, c, v = int(r) - 1, int(c) - 1, int(v)
    beads.append((v, i, r, c, d))

direction_map = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
opposite_direction = {'U': 'D', 'D': 'U', 'L': 'R', 'R': 'L'}
max_weight = -sys.maxsize

def in_range(r, c):
    return (0 <= r < n and 0 <= c < n)

for _ in range(t):
    cnt = len(beads)
    moved_map = [[[] for _ in range(n)] for _ in range(n)]
    positions = set()

    for _ in range(cnt):
        v, idx, r, c, d = beads.popleft()

        for _ in range(v):
            dr, dc = direction_map[d]
            new_r, new_c = r + dr, c + dc
            if not in_range(new_r, new_c):
                d = opposite_direction[d]
                dr, dc = direction_map[d]
                new_r, new_c = r + dr, c + dc
            r, c = new_r, new_c

        heapq.heappush(moved_map[r][c], (-v, -idx, r, c, d))
        positions.add((r, c))

    for i, j in positions:
        cnt = len(moved_map[i][j])
        for _ in range(min(cnt, k)):
            v, idx, r, c, d = heapq.heappop(moved_map[i][j])            
            beads.append((-v, -idx, r, c, d))

print(len(beads))