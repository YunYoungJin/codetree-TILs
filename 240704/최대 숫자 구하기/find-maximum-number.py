from sortedcontainers import SortedSet

n, m = map(int, input().split())
arr = list(map(int, input().split()))
s = SortedSet([i for i in range(1, m + 1)])

for elem in arr:
    s.remove(elem)
    print(s[-1])