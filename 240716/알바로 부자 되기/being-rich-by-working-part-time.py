n = int(input())
alba_infos = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

# 1~ i 번째 알바를 고려할 때 가장 많이 벌 수 있는 금액
dp = [0] * (n)
dp[0] = alba_infos[0][2]

for i in range(1, n):
    s, e, p = alba_infos[i]

    for j in range(i):
        ps, pe, pp = alba_infos[j]
        # 이전 알바와 병행이 불가능하다면
        # 현재 알바를 고르는 것이 나은 것인지 아닌지 확인
        if pe >= s:
            dp[i] = max(p, dp[i])
            
        # 이전 알바와 병행이 가능하다면
        # 더 많이 벌게되는 금액을 입력
        else:
            dp[i] = max(dp[i], dp[j] + p)

print(max(dp))