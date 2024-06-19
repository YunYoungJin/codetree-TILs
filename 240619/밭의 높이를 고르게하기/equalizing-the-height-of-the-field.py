import sys

n, h, t = map(int, input().split())

arr = list(map(int, input().split()))

min_cost = sys.maxsize

for i in range(len(arr) - t + 1):
    cost = 0
    for j in range(i, i + t):
        if j >= len(arr) - 1:
            break
        cost += abs(h - arr[j])
    min_cost = min(min_cost, cost)
print(min_cost)