import sys
INF = sys.maxsize

n = int(input())
base = " " + input()
target = " " + input()

dp = [[INF for _ in range(10)] for _ in range(n + 1)]
dp[0][0] = 0

for i in range(n):
    for j in range(10):
        if dp[i][j] == INF:
            continue
        
        current_digit = (int(base[i + 1]) + j) % 10
        target_digit = int(target[i + 1])

        # 반시계 방향 회전
        cost = (target_digit - current_digit + 10) % 10
        nj = (j + cost) % 10
        dp[i + 1][nj] = min(dp[i + 1][nj], dp[i][j] + cost)

        # 시계 방향 회전
        cost = (current_digit - target_digit + 10) % 10
        nj = j
        dp[i + 1][nj] = min(dp[i + 1][nj], dp[i][j] + cost)

ans = min(dp[n])

print(ans)