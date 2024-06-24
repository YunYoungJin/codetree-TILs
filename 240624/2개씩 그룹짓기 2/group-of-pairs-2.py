import sys

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

max_min_diff = sys.maxsize

for i in range(n):
    max_min_diff = min(max_min_diff, arr[i + n] - arr[i])

print(max_min_diff)