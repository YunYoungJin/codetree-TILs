n = int(input())
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

max_cnt = 0
# 같은 행
for i in range(n):
    for j in range(n - 5):
        cnt1 = arr[i][j] + arr[i][j + 1] + arr[i][j + 2]
        for k in range(j + 3, n - 2):
            cnt2 = arr[i][k] + arr[i][k + 1] + arr[i][k + 2]
            max_cnt = max(max_cnt, cnt1 + cnt2)

# 다른 행
for i in range(n - 1):
    for j in range(n - 2):
        cnt1 = arr[i][j] + arr[i][j + 1] + arr[i][j + 2]
        for k in range(i + 1, n):
            for l in range(n - 2):
                cnt2 = arr[k][l] + arr[k][l + 1] + arr[k][l + 2]
                max_cnt = max(max_cnt, cnt1 + cnt2)

print(max_cnt)