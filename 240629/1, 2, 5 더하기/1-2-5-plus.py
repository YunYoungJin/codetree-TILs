n = int(input())
nums = [1, 2, 5]

dp = [0] * (n + 1)
dp[0] = 1

for i in range(1, n + 1):
    for num in nums:
        if i >= num:
            dp[i] += dp[i - num]

print(dp[n] % 10007)