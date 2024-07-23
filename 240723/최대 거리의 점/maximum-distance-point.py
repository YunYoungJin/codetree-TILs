n, m = map(int, input().split())
xs = [
    int(input())
    for _ in range(n)
]

xs.sort()

def place_items(x):
    cnt = 1
    last_pos = xs[0]

    for i in range(1, n):
        if xs[i] - last_pos >= x:
            cnt += 1
            last_pos = xs[i]

            if cnt >= m:
                return True
    
    return False

# 두 물건의 최소 거리
left = 1
# 두 물건의 최대 거리
right = xs[n - 1] - xs[0]
ans = 0

while left <= right:
    # 가장 인접한 두 물건의 거리가 mid라고 하자.
    mid = (left + right) // 2

    # 거리를 유지하면서 아이템을 배치할 수 있으면
    if place_items(mid):
        ans = mid
        left = mid + 1
    else:
        right = mid - 1

print(ans)