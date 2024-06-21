n, m = map(int, input().split())
arr = list(map(int, input().split()))

ans = 0

# 모든 시작 위치 시도
for k in range(n):
    pos = k
    tmp = 0
    # 움직임은 m번
    for _ in range(m):
        tmp += arr[pos]
        pos = arr[pos] - 1
    
    ans = max(ans, tmp)

print(ans)