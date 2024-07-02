import sys

n, k = map(int, input().split())
arr = [0] + list(map(int, sys.stdin.readline().split()))

INT_MIN = -sys.maxsize

ans = INT_MIN

# 현 위치까지의 최대합, 선택한 음수의 개수
dp = [[INT_MIN] * (k + 1) for _ in range(n + 1)]

for t in range(k + 1):
    dp[0][t] = 0

for i in range(1, n + 1):
    if arr[i] >= 0:
        for j in range(k + 1):
            dp[i][j] = max(dp[i - 1][j] + arr[i], arr[i])
            ans = max(ans, dp[i][j])
    else:
        for j in range(1, k + 1):
            dp[i][j] = max(dp[i - 1][j - 1] + arr[i], arr[i])
            ans = max(ans, dp[i][j])

print(ans)