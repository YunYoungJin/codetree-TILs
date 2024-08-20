import sys
import heapq
from collections import deque, defaultdict

input = sys.stdin.readline

offset = 2000
t = int(input())
direction_map = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}

for _ in range(t):
    n = int(input())
    beads = deque()
    ans = -1

    for i in range(1, n + 1):
        x, y, w, d = input().split()
        x, y, w = 2 * int(x) + offset, 2 * int(y) + offset, int(w)
        beads.append((w, i, x, y, d))

    for time in range(1, 4001):
        moved_map = defaultdict(list)
        
        for _ in range(len(beads)):
            w, idx, x, y, d = beads.popleft()

            dx, dy = direction_map[d]
            new_x, new_y = x + dx, y + dy

            if -2000 + offset <= new_x <= 2000 + offset and -2000 + offset <= new_y <= 2000 + offset:
                heapq.heappush(moved_map[(new_x, new_y)], (-w, -idx, d))

        for key in moved_map:
            if len(moved_map[key]) >= 2:
                ans = time
            w, idx, d = heapq.heappop(moved_map[key])
            beads.append((-w, -idx, key[0], key[1], d))

    print(ans)