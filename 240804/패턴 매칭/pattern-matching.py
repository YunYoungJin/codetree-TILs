s = input()
p = input()

m, n = len(s), len(p)

# dp[i][j] s[0:i] p[0:j] 매칭 여부
# DP 테이블 초기화
dp = [[False] * (n + 1) for _ in range(m + 1)]

# 빈 문자열과 빈 패턴은 매칭됨
dp[0][0] = True

# 패턴이 빈 문자열과 매칭되는 경우 초기화
for j in range(2, n + 1):
    if p[j - 1] == '*':
        dp[0][j] = dp[0][j - 2]

# DP 테이블 채우기
for i in range(1, m + 1):
    for j in range(1, n + 1):
        if p[j - 1] == '*':
            # 첫 번째 조건: '*'와 그 앞의 문자 'p[j-2]'가 0번 매칭되는 경우
            dp[i][j] = dp[i][j - 2]

            # 두 번째 조건: s[i-1]가 p[j-2]와 매칭되거나, p[j-2]가 '.'인 경우
            # 그리고 dp[i-1][j]가 True이면 현재 '*'와 그 앞의 문자가 1번 이상 매칭되는 경우
            if s[i - 1] == p[j - 2] or p[j - 2] == '.':
                dp[i][j] = dp[i][j] or dp[i - 1][j]
        else:
            # p[j-1]이 '*'이 아닌 경우
            # 현재 문자가 매칭되는지 확인
            if s[i - 1] == p[j - 1] or p[j - 1] == '.':
                dp[i][j] = dp[i - 1][j - 1]

if dp[m][n]:
    print("true")
else:
    print("false")