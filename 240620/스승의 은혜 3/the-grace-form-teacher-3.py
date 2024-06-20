n, b = map(int, input().split())

p_list = [
    list(map(int, input().split()))
    for _ in range(n)
]

ans = 0

# 쿠폰 사용 대상 지정
for i in range(n):
    tmp = p_list.copy()
    tmp[i][0] //= 2
    tmp.sort(key = lambda x : x[0] + x[1])
    cost = b
    cnt = 0
    for j in range(n):
        cost -= (tmp[j][0] + tmp[j][1])
        if cost >= 0:
            cnt += 1
        else:
            break
    ans = max(ans, cnt)
print(ans)