n = int(input())
infos = [(0, 0, 0)] + [
    tuple(map(int, input().split()))
    for _ in range(n)
]

dp = [[0] * 3 for _ in range(n + 1)]

dp[1][0] = infos[1][0]
dp[1][1] = infos[1][1]
dp[1][2] = infos[1][2]

for i in range(2, n + 1):
    dp[i][0] = max(dp[i - 1][1], dp[i - 1][2]) + infos[i][0]
    dp[i][1] = max(dp[i - 1][0], dp[i - 1][2]) + infos[i][1]
    dp[i][2] = max(dp[i - 1][0], dp[i - 1][1]) + infos[i][2]

print(max(dp[n]))