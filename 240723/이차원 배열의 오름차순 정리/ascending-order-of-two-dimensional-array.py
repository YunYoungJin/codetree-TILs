n = int(input())
k = int(input())

left = 1
right = n ** 2

def count_less_equal(x, n):
    cnt = 0
    for i in range(1, n + 1):
        cnt += min(n, x // i)
    return cnt

while left < right:
    mid = (left + right) // 2
    if count_less_equal(mid, n) < k:
        left = mid + 1
    else:
        right = mid

print(left)