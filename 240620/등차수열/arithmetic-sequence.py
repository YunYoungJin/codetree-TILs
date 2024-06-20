n = int(input())
arr = list(map(int, input().split()))

max_cnt = 0

for k in range(101):
    cnt = 0
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == 2 * k:
                cnt += 1
    max_cnt = max(max_cnt, cnt)
print(max_cnt)