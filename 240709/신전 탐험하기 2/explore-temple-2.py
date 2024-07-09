n = int(input())
infos = [(0, 0, 0)] + [
    tuple(map(int, input().split()))
    for _ in range(n)
]

# i 방향으로 시작했을때 j층에서 k방향 방을 선택했을때의 보물 최댓값
dp = [[[-1] * 3 for _ in range(1001)] for _ in range(3)]

dp[0][1][0] = infos[1][0]
dp[1][1][1] = infos[1][1]
dp[2][1][2] = infos[1][2]


for i in range(3):
    for j in range(2, n + 1):
        # j 층에서 고른 방
        for k in range(3):
            # j - 1층에서 고른 방
            for l in range(3):
                if k == l:
                    continue
                dp[i][j][k] = max(dp[i][j][k], dp[i][j - 1][l] + infos[j][k])
                

ans = 0        
for i in range(3):
    for j in range(3):
        if i != j:
            ans = max(ans, dp[i][n][j])
print(ans)