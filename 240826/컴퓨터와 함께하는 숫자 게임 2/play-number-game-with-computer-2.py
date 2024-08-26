import sys

m = int(input())
a, b = map(int, input().split())

shortest, longest = sys.maxsize, -sys.maxsize

for target in range(a, b + 1):
    left, right = 1, m
    cnt = 0

    while left <= right:
        mid = (left + right) // 2
        cnt += 1

        if mid == target:
            shortest = min(shortest, cnt)
            longest = max(longest, cnt)
            break

        if mid > target:
            right = mid - 1
        else:
            left = mid + 1

print(shortest, longest)