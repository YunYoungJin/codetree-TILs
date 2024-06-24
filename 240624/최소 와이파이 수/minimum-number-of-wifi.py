n, m = map(int, input().split())
line = list(map(int, input().split()))


# 사람이 한명도 살지 않으면
if line.count(1) == 0:
    print(0)
# 사람이 한명만 살거나, 와이파이 1개로 해결이 된다면
elif line.count(1) == 1 or m >= n - 1:
    print(1)
else:
    ans = 0
    pos = 0

    while pos < n:
        # 사람이 사는 집 찾기
        if line[pos] != 1:
            pos += 1
        
        if pos + m <= n - 1:
            ans += 1
            pos += 2 * m + 1

    print(ans)