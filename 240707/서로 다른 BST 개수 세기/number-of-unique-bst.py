n = int(input())

dp = [0] * 20

dp[0] = 1
dp[1] = 1
dp[2] = 2

for i in range(3, n + 1):
    tmp = 0 
    for j in range(i):
        tmp += dp[j] * dp[i - j - 1] 
    dp[i] = tmp

print(dp[n])