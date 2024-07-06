import sys
from sortedcontainers import SortedSet

n, m = map(int, input().split())
arr = list(map(int, sys.stdin.readline().split()))
s = SortedSet(range(1, m + 1))

ans = 0

for num in arr:
    idx = s.bisect_right(num)

    if idx != 0:
        idx -= 1
        s.remove(s[idx])

        ans += 1
    else:
        break

print(len(s))