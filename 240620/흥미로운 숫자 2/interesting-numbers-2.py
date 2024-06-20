x, y = map(int, input().split())

cnt = 0
for num in range(x, y + 1):
    tmp = list(set(str(num)))
    
    if len(tmp) != 2:
        continue
    
    for digit in tmp:
        if str(num).count(digit) == 1:
            cnt += 1
print(cnt)