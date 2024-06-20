x, y = map(int, input().split())

ans = 0
for num in range(x, y + 1):
    num = str(num)
    tmp = 0
    for i in num:
        tmp += int(i)
    ans = max(ans, tmp)
print(ans)