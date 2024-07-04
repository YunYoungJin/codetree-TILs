import sys
INT_MIN = -sys.maxsize
n = int(input())
arr = list(map(int, input().split()))

tmp_sum = 0
ans = INT_MIN

for i in range(n):
    tmp_sum += arr[i]

    ans = max(ans, tmp_sum)

    if tmp_sum < 0:
        tmp_sum = 0

print(ans)