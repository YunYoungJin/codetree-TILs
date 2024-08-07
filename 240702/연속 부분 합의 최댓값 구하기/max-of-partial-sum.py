import sys

INT_MIN = -sys.maxsize

n = int(input())
arr = list(map(int, sys.stdin.readline().split()))

dp = [INT_MIN] * n
dp[0] = arr[0]

for i in range(1, n):
    dp[i] = max(dp[i - 1] + arr[i], arr[i])

print(max(dp))