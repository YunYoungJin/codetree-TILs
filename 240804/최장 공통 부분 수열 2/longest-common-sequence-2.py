A = list(input())
B = list(input())

n = len(A)
m = len(B)

dp = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if A[i - 1] == B[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

# LCS 추적
i, j = n, m
lcs = []

while i > 0 and j > 0:
    if A[i - 1] == B[j - 1]:
        lcs.append(A[i - 1])
        i -= 1
        j -= 1
    elif dp[i - 1][j] >= dp[i][j - 1]:
        i -= 1
    else:
        j -= 1

# LCS는 뒤에서부터 추적했으므로, 역순으로 바꿔야 함
lcs.reverse()

print(''.join(lcs))