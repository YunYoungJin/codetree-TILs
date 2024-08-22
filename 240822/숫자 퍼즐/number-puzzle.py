import sys
INF = sys.maxsize

n, m, target = map(int, input().split())

# i번째 마법석까지, 숫자들의 합이 j일 때, 현재 마법석의 숫자가 l
dp = [[[0 for _ in range(m + 1)] for _ in range(m + 1)] for _ in range(n + 1)]

for i in range(1, m + 1):
    dp[1][i][i] = 1

for i in range(1, n):
    for j in range(1, m + 1):
        for k in range(1, m + 1):
            for l in range(1, k + 1):
                if j + l > m:
                    break
                dp[i + 1][j + l][l] += dp[i][j][k]
                dp[i + 1][j + 1][l] = min(dp[i + 1][j + l][l], INF)

cur_l = 1
cur_m = m

for i in range(n, 0, -1):
    while dp[i][cur_m][cur_l] < target:
        target -= dp[i][cur_m][cur_l]
        cur_l += 1
    print(cur_l, end=' ')
    cur_m -= cur_l