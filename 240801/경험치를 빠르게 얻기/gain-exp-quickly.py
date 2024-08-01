import sys

INT_MAX = sys.maxsize

n, m = map(int, input().split())
quests = [(0, 0)] + [
    tuple(map(int, input().split()))
    for _ in range(n)
]

max_exp = sum(e for e, _ in quests)
dp = [
    [INT_MAX for _ in range(max_exp + 1)]
    for _ in range(n + 1)
]

dp[0][0] = 0

# i번째 퀘스트까지 고려
# 지금까지 얻은 경험치 합이 j
# 걸리는 최소 시간을 계산
for i in range(1, n + 1):
    e, t = quests[i]
    for j in range(0, max_exp + 1):
        if j >= e:
            dp[i][j] = min(dp[i - 1][j - e] + t, dp[i - 1][j])
        else:
            dp[i][j] = dp[i - 1][j]

ans = INT_MAX
for exp in range(m, max_exp + 1):
    ans = min(ans, dp[n][exp])

if ans == INT_MAX:
    print(-1)
else:
    print(ans)