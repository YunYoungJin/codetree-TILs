import sys

n, k = map(int, input().split())
arr = list(map(int, input().split()))
min_cost = sys.maxsize

# 최대 최소 차가 k 이하인 구간
for i in range(1, 10001 - k):
    tmp_cost = 0
    for num in arr:
        if i <= num and num <= i + k:
            continue
        elif num < i:
            tmp_cost += abs(i - num)
        elif num > i + k:
            tmp_cost += abs(num - i - k)
    min_cost = min(min_cost, tmp_cost)
print(min_cost)