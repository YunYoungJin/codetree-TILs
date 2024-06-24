n = int(input())
arr = list(map(int, input().split()))

odd_cnt = 0
even_cnt = 0

for num in arr:
    if num % 2 == 0:
        even_cnt += 1
    else:
        odd_cnt += 1

ans = 0

if even_cnt > odd_cnt:
    ans = odd_cnt * 2 + 1
elif even_cnt == odd_cnt:
    ans = even_cnt + odd_cnt
else:
    ans = even_cnt * 2
    remain_odd = odd_cnt - even_cnt
    if remain_odd % 3 == 0:
        ans += (remain_odd // 3) * 2
    elif remain_odd % 3 == 1:
        ans += (remain_odd // 3) * 2 - 1
    elif remain_odd % 3 == 2:
        ans += (remain_odd // 3) * 2 + 1

print(ans)