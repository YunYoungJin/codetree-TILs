import sys

n = int(input())
arr = list(map(int, input().split()))

min_dist = sys.maxsize

for i in range(1, n + 1):
    dist = 0
    for j in range(1, n + 1):
        dist += abs(i - j)  * arr[j - 1]
    if dist < min_dist:
        min_dist = dist
print(min_dist)