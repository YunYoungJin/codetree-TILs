n = int(input())
infos = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

# dp[i][j][k] - i번째 학생까지 고려할 때 축구팀 j명, 야구팀 k명 선택한 최대 능력 합
dp = [[[-1] * 10 for _ in range(12)] for _ in range(n + 1)]

dp[0][0][0] = 0

for i in range(1, n + 1):
    s, b = infos[i - 1]
    for j in range(12):
        for k in range(10):
            if dp[i - 1][j][k] != -1:
                # 현재 학생을 미배정
                dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j][k])
                
                # 현재 학생을 축구팀에 배정
                if j < 11:
                    dp[i][j + 1][k] = max(dp[i][j + 1][k], dp[i - 1][j][k] + s)
                
                # 현재 학생을 야구팀에 배정
                if k < 9:
                    dp[i][j][k + 1] = max(dp[i][j][k + 1], dp[i - 1][j][k] + b)

print(dp[n][11][9])