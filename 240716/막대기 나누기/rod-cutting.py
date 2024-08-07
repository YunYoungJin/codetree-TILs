n = int(input())
costs = [0] + list(map(int, input().split()))

dp = [0] * (n + 1)
dp[1] = costs[1]

for i in range(2, n + 1):
    for j in range(1, i + 1):
        dp[i] = max(dp[i], dp[i - j] + costs[j])

print(dp[n])