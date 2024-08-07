n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# A가 i장 B가 j장 버렸을 때 B가 받을 수 있는 최고 점수
dp = [[-1] * (n + 1) for _ in range(n + 1)]

# 0장 버렸을 때는 0점
dp[0][0] = 0

for i in range(n):
    for j in range(n):
        if dp[i][j] == -1:
            continue

        # 둘의 카드가 같거나, 그냥 버리기로 결정했다면
        dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j])

        # B 점수가 더 낮으면 B의 카드를 버리고 점수를 얻을 수 있음
        if B[j] < A[i]:
            dp[i][j + 1] = max(dp[i][j + 1], dp[i][j] + B[j])

        if B[j] > A[i]:
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])


ans = 0
for i in range(n + 1):
    ans = max(ans, dp[i][n])
    ans = max(ans, dp[n][i])

print(ans)