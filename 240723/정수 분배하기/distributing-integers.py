n, m = map(int, input().split())
integers = [
    int(input())
    for _ in range(n)
]

left = 1
right = sum(integers) // m
ans = 0

def is_possible(k):
    cnt = 0
    for num in integers:
        cnt += num // k
    
    if cnt >= m:
        return True
    else:
        return False


while left <= right:
    mid = (left + right) // 2
    if is_possible(mid):
        left = mid + 1
        ans = max(ans, mid)
    else:                               
        right = mid - 1

print(ans)