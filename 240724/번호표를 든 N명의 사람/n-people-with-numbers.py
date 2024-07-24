import heapq

n, t = map(int, input().split())
ds = [
    int(input())
    for _ in range(n)
]

left = 1
right = n
ans = 10001

def is_possible(x):
    stage = []
    time = 0

    for i in range(n):
        if len(stage) < x:
            heapq.heappush(stage, ds[i])
        else:
            last_t = heapq.heappop(stage)
            time = last_t
            heapq.heappush(stage, time + ds[i])
    
    while len(stage) > 0:
        last_t = heapq.heappop(stage)
        time = last_t
    
    return time <= t


while left <= right:
    mid = (left + right) // 2

    if is_possible(mid):
        right = mid - 1
        ans = min(ans, mid)
    else:
        left = mid + 1

print(ans)