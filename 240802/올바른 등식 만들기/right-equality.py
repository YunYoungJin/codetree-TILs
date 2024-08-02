import sys

INT_MAX = sys.maxsize

n, m = map(int, input().split())
arr = list(map(int, input().split()))

# i: i번째 숫자까지 고려
# j: 해당 숫자를 -하면 0, + 하면 1
# k: 합이 -20~20 -> 0 ~ 40
dp = [[[0] * 41 for _ in range(2)] for _ in range(n)]
offset = 20

dp[0][0][offset - arr[0]] = 1
dp[0][1][offset + arr[0]] = 1

for i in range(1, n):
    num = arr[i]
    for j in range(41):
        if 0 <= j + num <= 40:
            dp[i][1][j + num] += dp[i - 1][1][j]
            dp[i][1][j + num] += dp[i - 1][0][j]
        if 0 <= j - num <= 40:
            dp[i][0][j - num] += dp[i - 1][1][j]
            dp[i][0][j - num] += dp[i - 1][0][j]

print(dp[n - 1][1][m + offset] + dp[n -1][0][m + offset])