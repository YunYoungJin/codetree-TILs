import sys
n, k = map(int, input().split())
arr = list(map(int, sys.stdin.readline().split()))

d = dict()

for num in arr:
    if num not in d:
        d[num] = 1
    else:
        d[num] += 1

top_k = [num for (num, _) in sorted(d.items(), key=lambda x: (-x[1], -x[0]))[:k]]
print(*top_k)