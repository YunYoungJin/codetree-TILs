n, m = map(int, input().split())
infos = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

# 무게의 합이 i 이하, 얻을 수 있는 최대 가치
dp = [0] * (m + 1)

for i in range(1, m + 1):
    for w, v in infos:
        if i >= w:
            dp[i] = max(dp[i - w] + v, dp[i])

print(max(dp))