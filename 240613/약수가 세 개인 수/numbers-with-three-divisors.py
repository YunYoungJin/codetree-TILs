start, end = map(int, input().split())
cnt = 0

for i in range(start, end + 1):
    cnt_cd = 0
    for j in range(1, i + 1):
        if i % j == 0:
            cnt_cd += 1
    if cnt_cd == 3:
        cnt += 1
print(cnt)