import sys

INT_MIN = -sys.maxsize

n, m = map(int, input().split())

# i번째 날, j번 옷을 입을 때의 화려함
clothes = [[0] * (n + 1) for _ in range(m + 1)]

# i번째 날, j번 옷을 입을 때의 만족도 최댓값
dp = [[INT_MIN] * (n + 1) for _ in range(m + 1)]

# 첫번째 날은 무얼 입어도 만족도 0
for i in range(1, n + 1):
    dp[1][i] = 0

for j in range(1, n + 1):
    s, e, v = map(int, input().split())
    for i in range(s, e + 1):
        clothes[i][j] = v
    

for day in range(2, m + 1):
    # 오늘 입을 옷
    for i in range(1, n + 1):
        if clothes[day][i] == 0:
            continue
        # 어제 입은 옷
        for j in range(1, n + 1):
            if clothes[day - 1][j] == 0:
                continue
            dp[day][i] = max(dp[day - 1][j] + abs(clothes[day][i] - clothes[day - 1][j]), dp[day][i])

print(max(dp[m]))