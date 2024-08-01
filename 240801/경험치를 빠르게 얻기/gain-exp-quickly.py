import sys

INT_MAX = sys.maxsize

n, m = map(int, input().split())
quests = [(0, 0)] + [
    tuple(map(int, input().split()))
    for _ in range(n)
]

max_exp = max(sum(e for e, _ in quests), m)
dp = [INT_MAX] * (max_exp + 1)
dp[0] = 0

for e, t in quests:
    for j in range(max_exp, e -1, -1):
        if dp[j - e] != INT_MAX:
            dp[j] = min(dp[j], dp[j - e] + t)

ans = min(dp[m:])

if ans == INT_MAX:
    print(-1)
else:
    print(ans)