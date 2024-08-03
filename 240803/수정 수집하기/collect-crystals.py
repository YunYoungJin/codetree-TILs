n, k = map(int, input().split())
gen_pos = list(input())

# i번째 수정을 고려할 때
# 현재까지 j번 이동했을 때
# k: 0이면 왼쪽, 1이면 오른쪽을 선택했을때 얻을 수 있는 수정 개수
dp = [[[0] * 2 for _ in range(k + 1)] for _ in range(n)]

dp[0][0][0] = 1 if gen_pos[0] == 'L' else 0
dp[0][1][1] = 1 if gen_pos[0] == 'R' else 0

for i in range(1, n):
    for j in range(k + 1):
        if gen_pos[i] == 'L':
            dp[i][j][0] = dp[i - 1][j][0] + 1  # 이동하지 않고 왼쪽에 계속 있는 경우
            dp[i][j][1] = dp[i - 1][j][1]  # 이동하지 않고 오른쪽에 계속 있는 경우
            if j > 0:
                dp[i][j][0] = max(dp[i][j][0], dp[i - 1][j - 1][1] + 1)  # 오른쪽에서 이동해온 경우
                dp[i][j][1] = max(dp[i][j][1], dp[i - 1][j - 1][0])  # 왼쪽에서 이동해온 경우
        else:
            dp[i][j][1] = dp[i - 1][j][1] + 1  # 이동하지 않고 오른쪽에 계속 있는 경우
            dp[i][j][0] = dp[i - 1][j][0]  # 이동하지 않고 왼쪽에 계속 있는 경우
            if j > 0:
                dp[i][j][1] = max(dp[i][j][1], dp[i - 1][j - 1][0] + 1)  # 왼쪽에서 이동해온 경우
                dp[i][j][0] = max(dp[i][j][0], dp[i - 1][j - 1][1])  # 오른쪽에서 이동해온 경우

# 결과 계산
ans = 0
for j in range(k + 1):
    ans = max(ans, dp[n - 1][j][0], dp[n - 1][j][1])

print(ans)