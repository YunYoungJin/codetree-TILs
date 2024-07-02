n = int(input())
mod = 1000000007

# i번째 자리수에 j를 골랐을 때 가능한 계단 수 개수
dp = [[0] * 10 for _ in range(n + 1)]

for i in range(1, 10):
    dp[1][i] = 1

for i in range(2, n + 1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i - 1][1]
        elif j == 9:
            dp[i][j] = dp[i - 1][8]
        else:
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]

ans = 0
for i in range(10):
    ans += dp[n][i]
print(ans % mod)