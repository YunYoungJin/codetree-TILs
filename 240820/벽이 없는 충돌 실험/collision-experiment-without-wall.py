import sys
import heapq
from collections import deque, defaultdict

input = sys.stdin.readline

t = int(input())
direction_map = {'U': (0, 0.5), 'D': (0, -0.5), 'L': (-0.5, 0), 'R': (0.5, 0)}

for _ in range(t):
    n = int(input())
    beads = deque()
    ans = -1

    for i in range(1, n + 1):
        x, y, w, d = input().split()
        x, y, w = int(x), int(y), int(w)
        beads.append((w, i, x, y, d))

    for time in range(1, 4002):
        moved_map = defaultdict(list)
        positions = set()

        for _ in range(len(beads)):
            w, idx, x, y, d = beads.popleft()

            dx, dy = direction_map[d]
            new_x, new_y = x + dx, y + dy

            if -2000 <= new_x <= 2000 and -2000 <= new_y <= 2000:
                heapq.heappush(moved_map[(new_x, new_y)], (-w, -idx, d))
                positions.add((new_x, new_y))

        for pos in positions:
            if len(moved_map[pos]) >= 2:
                ans = time
            w, idx, d = heapq.heappop(moved_map[pos])
            beads.append((-w, -idx, pos[0], pos[1], d))

    print(ans)