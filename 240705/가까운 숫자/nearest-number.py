import sys
from sortedcontainers import SortedSet

n = int(input())
arr = list(map(int, input().split()))
s = SortedSet()
s.add(0)
dist = sys.maxsize

for num in arr:
    s.add(num)
    big_idx = s.bisect_right(num)
    small_idx = big_idx - 2

    new_dist2 = sys.maxsize

    if big_idx != len(s):
        new_dist2 = s[big_idx] - num
    
    new_dist1 = num - s[small_idx]

    dist = min(dist, new_dist1, new_dist2)
    print(dist)