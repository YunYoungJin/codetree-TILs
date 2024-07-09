from sortedcontainers import SortedSet

n, m = map(int, input().split())
arr = list(map(int, input().split()))
query = list(map(int, input().split()))

s = SortedSet(arr)

for num in query:
    idx = s.bisect_right(num)

    if idx - 1 < 0:
        print(-1)
    else:
        print(s[idx - 1])
        s.remove(s[idx - 1])