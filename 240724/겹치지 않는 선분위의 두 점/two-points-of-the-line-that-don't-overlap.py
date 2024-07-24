n, m = map(int, input().split())
segments = [
    tuple(map(int, input().split()))
    for _ in range(m)
]

segments.sort()


def can_place_points(x):
    cnt = 1
    last_pos = segments[0][0]

    for i in range(m):
        a, b = segments[i]
        j = a
        if j - last_pos < x:
            j = last_pos + x
        while j <= b:
            cnt += 1
            last_pos = j
            j += x

    return cnt >= n


# 두 점의 최소 거리
left = 1
# 두 점의 최대 거리
right = segments[m - 1][1] - segments[0][0]
ans = 0

while left <= right:
    # 가장 인접한 두 점의 거리
    mid = (left + right) // 2

    # 거리를 유지하면서 점을 배치할 수 있으면
    if can_place_points(mid):
        ans = mid
        left = mid + 1
    else:
        right = mid - 1

print(ans)