n = int(input())

# i : 현재 출근 일 수
# t : t 받은 횟수
# b : 연속으로 받은 b의 수
dp = [[[0] * 3 for _ in range(3)] for _ in range(n + 1)]

# 1일차 G
dp[1][0][0] = 1
# 1일차 B
dp[1][0][1] = 1
# 1일차 T
dp[1][1][0] = 1

for i in range(2, n + 1):
    # i일차에 G를 받는 다면
    for t in range(3):
        for b in range(3):
            dp[i][t][0] += dp[i - 1][t][b]
    
    # i일차에 B를 받는 다면
    for t in range(3):
        for b in range(2):
            dp[i][t][b + 1] = dp[i - 1][t][b]

    # i일차에 T를 받는 다면
    for t in range(1, 3):
        for b in range(3):
            dp[i][t][0] += dp[i - 1][t - 1][b]

ans = 0
for t in range(3):
    for b in range(3):
        ans += dp[n][t][b]

print(ans % (10 ** 9 + 7))