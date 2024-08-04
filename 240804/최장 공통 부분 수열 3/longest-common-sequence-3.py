n, m = map(int, input().split())
a = list(map(int ,input().split()))
b = list(map(int, input().split()))

dp = [[0] * (m + 1) for _ in range(n + 1)]
path = [[''] * (m + 1) for _ in range(n + 1)]

# DP 테이블 채우기
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if a[i - 1] == b[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
            path[i][j] = 'diagonal'
        else:
            if dp[i - 1][j] > dp[i][j - 1]:
                dp[i][j] = dp[i - 1][j]
                path[i][j] = 'up'
            elif dp[i - 1][j] < dp[i][j - 1]:
                dp[i][j] = dp[i][j - 1]
                path[i][j] = 'left'
            else:
                dp[i][j] = dp[i - 1][j]
                path[i][j] = 'up' if a[i - 1] > b[j - 1] else 'left'

# LCS 추적
lcs = []
i, j = n, m
while i > 0 and j > 0:
    if path[i][j] == 'diagonal':
        lcs.append(a[i - 1])
        i -= 1
        j -= 1
    elif path[i][j] == 'up':
        i -= 1
    else:
        j -= 1

lcs.reverse()
print(' '.join(map(str, lcs)))