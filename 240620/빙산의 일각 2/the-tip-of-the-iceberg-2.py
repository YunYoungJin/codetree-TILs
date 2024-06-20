n = int(input())

ice = [
    int(input())
    for _ in range(n)
]
ans = 0

for h in range(1, 1001):
    cnt = 0
    is_new_chunk = True
    for i in range(n):
        if ice[i] - h <= 0:
            is_new_chunk = True
        elif ice[i] - h > 0:
            if is_new_chunk:
                is_new_chunk = False
                cnt += 1
            else:
                continue
    ans = max(ans, cnt)
   
print(ans)