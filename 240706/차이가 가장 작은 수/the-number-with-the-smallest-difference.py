from sortedcontainers import SortedSet
import sys

n, m = map(int, input().split())
arr = [
    int(sys.stdin.readline())
    for _ in range(n)
]

s = SortedSet(arr)
ans = sys.maxsize

for num in arr:
    min_idx = s.bisect_left(num + m)
    if min_idx != len(s):
        ans = min(ans, s[min_idx] - num)

if ans == sys.maxsize:
    ans = -1

print(ans)