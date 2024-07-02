n = int(input())
arr = [0] + list(map(int, input().split()))

# 각 층까지 1계단을 몇번 올랐는지에 따른 동전 습득량
dp = [[-1] * 4 for _ in range(n + 1)]

dp[0][0] = 0
dp[1][1] = arr[1]
dp[2][0] = arr[2]
dp[2][2] = arr[1] + arr[2]

for i in range(3, n + 1):
    if i % 2 == 1:
        dp[i][1] = max(dp[i - 2][1], dp[i - 1][0]) + arr[i]
        dp[i][3] = max(dp[i - 2][3], dp[i - 1][2]) + arr[i]
    else:
        dp[i][0] = dp[i - 2][0] + arr[i]
        dp[i][2] = max(dp[i - 2][2], dp[i - 1][1]) + arr[i]

print(max(dp[n]))