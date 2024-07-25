n, m, c = map(int, input().split())
arrival_times = list(map(int, input().split()))
arrival_times.sort()

left = 0
right = arrival_times[-1]
ans = right


def is_possible(mid):
    bus_cnt = 1
    people_cnt = 1
    first_person_time = arrival_times[0]

    for i in range(1, n):
        if people_cnt == c or arrival_times[i] - first_person_time > mid:
            bus_cnt += 1
            first_person_time = arrival_times[i]
            people_cnt = 1
        else:
            people_cnt += 1

    return bus_cnt <= m


while left <= right:
    mid = (left + right) // 2

    if is_possible(mid):
        right = mid - 1
        ans = min(ans, mid)
    else:
        left = mid + 1

print(ans)