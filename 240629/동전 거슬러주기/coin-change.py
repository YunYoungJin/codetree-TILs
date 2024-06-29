import sys
INT_MAX = sys.maxsize

n, m = map(int, input().split())
coins = [0] + list(map(int, input().split()))
coins.sort()

# 
dp = [0] + [INT_MAX] * m

for i in range(1, m + 1):
    for j in range(1, n + 1):
        if i >= coins[j]:
            if dp[i - coins[j]] == INT_MAX:
                continue
            dp[i] = min(dp[i], dp[i - coins[j]] + 1)

if dp[m] == INT_MAX:
    print(-1)
else:
    print(dp[m])