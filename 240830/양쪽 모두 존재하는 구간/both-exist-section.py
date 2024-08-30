import sys
from collections import defaultdict

n, m = map(int, input().split())
arr = list(map(int, input().split()))

total_count = defaultdict(int)
for num in arr:
    total_count[num] += 1

# 1부터 m까지 모든 숫자가 2개 이상 있는지 체크
if any(count < 2 for count in total_count.values()):
    print(-1)
    sys.exit()

j = 0
ans = sys.maxsize
interval_count = defaultdict(int)

for i in range(n):
    while j < n and len(interval_count) < m:
        if j == n:
            break
        interval_count[arr[j]] += 1
        total_count[arr[j]] -= 1
        if total_count[arr[j]] == 0:
            del total_count[arr[j]]
        j += 1

    if len(interval_count) == m and len(total_count) == m:
            ans = min(ans, j - i)

    total_count[arr[i]] += 1
    interval_count[arr[i]] -= 1
    if interval_count[arr[i]] == 0:
        del interval_count[arr[i]]

print(ans if ans != sys.maxsize else -1)