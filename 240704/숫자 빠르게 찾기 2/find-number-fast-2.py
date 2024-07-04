from sortedcontainers import SortedSet

n, m = map(int, input().split())
arr = list(map(int, input().split()))
s = SortedSet(arr)

for _ in range(m):
    idx = s.bisect_left(int(input()))
    if idx < len(s):
        print(s[idx])
    else:
        print(-1)