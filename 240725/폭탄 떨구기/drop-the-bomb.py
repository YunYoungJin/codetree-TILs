n, k = map(int, input().split())
points = [
    int(input())
    for _ in range(n)
]
points.sort()

def is_possible(mid):
    cnt = 0
    last_bomb_range = -1

    for i in range(n):
        if points[i] > last_bomb_range:
            last_bomb_range = points[i] + 2 * mid
            cnt += 1
    
    return cnt <= k

left = 0
right = 1000000000
ans = right

while left <= right:
    mid = (left + right) // 2

    if is_possible(mid):
        right = mid -1
        ans = min(ans, mid)
    else:
        left = mid + 1

print(ans)