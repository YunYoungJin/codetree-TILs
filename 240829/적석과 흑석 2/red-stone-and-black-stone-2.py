import sys
from sortedcontainers import SortedSet
input = sys.stdin.readline

c, n = map(int, input().split())
red_stones = []
black_stones = []

for _ in range(c):
    red_stones.append(int(input()))

for _ in range(n):
    a, b = map(int, input().split())
    black_stones.append((a, b))

red_stones.sort()
black_stones.sort(key=lambda x: x[1])

ans = 0
not_used = SortedSet(range(c))

for a, b in black_stones:
    if len(not_used) == 0:
        break

    red_idx = not_used[0]

    while red_idx < c and red_stones[red_idx] < a:
        red_idx += 1
    
    if red_idx < c and a <= red_stones[red_idx] <= b and red_idx in not_used:
        ans += 1
        not_used.remove(red_idx)
        red_idx += 1

print(ans)