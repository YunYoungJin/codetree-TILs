n, m = map(int, input().split())
arr = list(map(int, input().split()))

# i번째 인덱스의 수가
# j(1~4)일 때,
# 현재까지 인접한 수가 다른 횟수가 k번일 때 유사도
dp = [[[0] * (m + 1) for _ in range(5)] for _ in range(n)]

# 첫 번째 위치 초기화
for j in range(1, 5):
    if arr[0] == j:
        dp[0][j][0] = 1
    else:
        dp[0][j][0] = 0

for i in range(1, n):
    # i번째 수가 j이고
    for j in range(1, 5):
        for k in range(m + 1):
            # 바로 전 위치의 수가 p일 떄
            for p in range(1, 5):
                if p == j:
                    dp[i][j][k] = max(dp[i][j][k], dp[i - 1][p][k] + (1 if arr[i] == j else 0))
                elif k + 1 <= m:
                    dp[i][j][k + 1] =  max(dp[i][j][k + 1], dp[i - 1][p][k] + (1 if arr[i] == j else 0))

ans = 0
for j in range(1, 5):
    for k in range(m + 1):
        ans = max(ans, dp[n - 1][j][k])

print(ans)