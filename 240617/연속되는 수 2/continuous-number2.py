n = int(input())
arr= [int(input()) for _ in range(n)]

new = False
max_cnt = 0
cnt = 1

for i in range(1, n):
    if arr[i] != arr[i - 1]:
        max_cnt = max(max_cnt, cnt)
        cnt = 1
        new = True
    else:
        cnt += 1

if not new:
    print(len(arr))
else:
    print(max_cnt)