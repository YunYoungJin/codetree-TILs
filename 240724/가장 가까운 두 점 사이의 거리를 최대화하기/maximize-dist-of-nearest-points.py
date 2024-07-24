n = int(input())
segments = [
    tuple(map(int, input().split()))
    for _ in range(n)
]
segments.sort()

left = 1
right = segments[-1][1] - segments[0][0]
ans = 0

def is_possible(x):
    lp = segments[0][0]
    cnt = 1

    for i in range(1, n):
        s, e = segments[i]

        if s - lp < x:
            s = lp + x
        
        if s > e:
            continue

        if s - lp >= x:
            cnt += 1
            lp = s
        
        if cnt >= n:
            return True
    
    return False

while left <= right:
    # 가장 인접한 두 점의 거리
    mid = (left + right) // 2

    if is_possible(mid):
        ans = mid
        left = mid + 1
    else:
        right = mid - 1

print(ans)