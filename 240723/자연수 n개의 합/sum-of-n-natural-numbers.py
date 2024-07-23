s = int(input())

left = 1
right = s
ans = 0

while left <= right:
    mid = (left + right) // 2

    if (mid * (mid + 1)) // 2 <= s:
        ans = max(ans, mid)
        left = mid + 1
    else:
        right = mid -1

print(ans)