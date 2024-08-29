import sys
from sortedcontainers import SortedSet

input = sys.stdin.readline

c, n = map(int, input().split())
red_stones = SortedSet()
black_stones = []

for _ in range(c):
    red_stones.add(int(input()))

for _ in range(n):
    a, b = map(int, input().split())
    black_stones.append((a, b))

black_stones.sort(key=lambda x: (x[1], -x[0]))

ans = 0

for a, b in black_stones:
    # 빨간 돌이 남아있지 않으면 멈춤
    if not red_stones:
        break

    red_idx = red_stones.bisect_left(a)

    if red_idx < len(red_stones) and a <= red_stones[red_idx] <= b:
        ans += 1
        red_stones.pop(red_idx)

print(ans)