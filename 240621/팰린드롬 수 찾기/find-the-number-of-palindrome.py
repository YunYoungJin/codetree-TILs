x, y = map(int, input().split())

ans = 0

for num in range(x, y + 1):
    num = str(num)
    leng = len(num)
    is_pal = True

    for i in range(leng // 2 + 1):
        if num[i] != num[leng - 1 - i]:
            is_pal = False
            break
    
    if is_pal:
        ans += 1
print(ans)