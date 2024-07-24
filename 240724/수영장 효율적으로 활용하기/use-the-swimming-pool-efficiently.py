n, m = map(int, input().split())
ts = list(map(int, input().split()))

left = 1
right = sum(ts)
ans = 100001

def is_possible(x):
    cnt = 1
    time = 0

    for i in range(n):
        if ts[i] > x:
            return False
        elif time + ts[i] > x:
            time = ts[i]
            cnt += 1
        else:
            time += ts[i]
    
    return cnt <= m


while left <= right:
    # 레인 별 수영장 이용시간의 총합
    mid = (left + right) // 2

    if is_possible(mid):
        ans = min(ans, mid)
        right = mid - 1
    else:
        left = mid + 1

print(ans)