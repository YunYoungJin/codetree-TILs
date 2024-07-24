n, m = map(int, input().split())
pass_costs = [
    int(input())
    for _ in range(m)
]

pass_costs.sort()

left = 1
right = pass_costs[-1] * n
ans = right

def is_possible(x):
    cnt = 0
    for i in range(m):
        if x // pass_costs[i] >= 1:
            cnt += x // pass_costs[i]
        else:
            break
    
    return cnt >= n

while left <= right:
    mid = (left + right) // 2

    if is_possible(mid):
        right = mid - 1
        ans = min(ans, mid)
    else:
        left = mid + 1

print(ans)