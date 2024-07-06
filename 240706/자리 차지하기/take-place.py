import sys
from sortedcontainers import SortedSet

n, m = map(int, input().split())
arr = list(map(int, sys.stdin.readline().split()))
s = SortedSet()

for a in arr:
    can_sit = False
    for i in range(a, 0, -1):
        if i in s:
            continue
        else:
            can_sit = True
            s.add(i)
            break
    
    if not can_sit:
        break

print(len(s))