import sys

n, k = map(int, input().split())
arr = set(list(map(int, sys.stdin.readline().split())))

sorted_set = sorted(arr, reverse=True)

print(*sorted_set[:k])