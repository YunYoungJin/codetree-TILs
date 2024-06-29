import sys
INT_MIN = -sys.maxsize

n, m = map(int, input().split())
coins = [0] + list(map(int, input().split()))
coins.sort()

# 
dp = [0] + [INT_MIN] * m

for i in range(1, m + 1):
    for j in range(1, n + 1):
        if i >= coins[j]:
            if dp[i - coins[j]] == INT_MIN:
                continue
            dp[i] = max(dp[i], dp[i - coins[j]] + 1)

if dp[m] == INT_MIN:
    print(-1)
else:
    print(dp[m])