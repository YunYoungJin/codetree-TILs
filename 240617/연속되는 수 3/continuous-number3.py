n = int(input())
arr= [int(input()) for _ in range(n)]

max_len, cnt = 0, 0

for i in range(n):
    if i >= 1 and arr[i] * arr[i - 1] > 0:
        cnt += 1
    else:
        cnt = 1
    max_len = max(max_len, cnt)
print(max_len)