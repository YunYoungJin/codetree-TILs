import sys
INT_MIN = -sys.maxsize
n, m = map(int, input().split())
arr = [0] + list(map(int, input().split()))

# i 번째 숫자, j개의 구간일때 최댓값
dp = [[INT_MIN] * (m + 1) for _ in range(n + 1)]
dp[0][0] = 0

for j in range(1, m + 1):
    for i in range(1, n + 1):
        current_sum = 0
        for k in range(i, 0, -1):
            current_sum += arr[k]
            if j == 1:
                dp[i][j] = max(dp[i - 1][j], dp[i][j], current_sum)
            elif k >= 3:
                dp[i][j] = max(dp[i - 1][j], dp[i][j], dp[k - 2][j - 1] + current_sum)


print(dp[n][m])