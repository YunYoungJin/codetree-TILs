n, m = map(int, input().split())
infos = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

dp = [0] * (m + 1)

for i in range(1, m + 1):

    for w, v in infos:
        if i < w:
            continue
        else:
            dp[i] = max(dp[i], v)
            for j in range(i - w, i):
                dp[i] = max(dp[i - w] + v, dp[j], dp[i])

print(max(dp))