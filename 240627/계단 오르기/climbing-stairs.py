n = int(input())

dp = [-1] * (n + 1)
dp[1] = 0

def stair(n):
    if dp[n] != -1:
        return dp[n]
    if n <= 3: 
        dp[n] = 1
    else: 
        dp[n] = stair(n - 2) + stair(n - 3)
    return dp[n]

print(stair(n) % 10007)