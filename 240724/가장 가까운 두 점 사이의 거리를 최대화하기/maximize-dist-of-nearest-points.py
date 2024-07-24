n = int(input())
segments = [
    tuple(map(int, input().split()))
    for _ in range(n)
]
segments.sort()

left = 1
right = segments[-1][1]
ans = 0

def is_possible(x):
    lp = segments[0][0]

    _, e = segments[1]

    if segments[1][1] > segments[2][0]:
        e = segments[2][0] - 1
    
    return e - lp >= x

while left <= right:
    # 가장 인접한 두 점의 거리
    mid = (left + right) // 2

    if is_possible(mid):
        ans = mid
        left = mid + 1
    else:
        right = mid - 1

print(ans)