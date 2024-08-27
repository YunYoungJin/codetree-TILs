n, k, l = map(int, input().split())
cs = list(map(int, input().split()))
cs.sort(reverse=True)

def is_possible(mid):
    index = 0
    remain = k * l

    for c in cs:
        if c >= mid:
            index += 1
            continue
        elif mid - c <= k and remain >= mid - c:
            remain -= mid - c
            index += 1
        else:
            break        
    
    return index >= mid

left = 0
right = n
ans = 0

while left <= right:
    mid = (left + right) // 2

    if is_possible(mid):
        left = mid + 1
        ans = max(ans, mid)
    else:
        right = mid - 1

print(ans)