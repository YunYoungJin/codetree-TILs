n = int(input())
moving_costs = list(map(int, input().split()))
refill_costs = list(map(int, input().split()))

min_rf = [1000001] * n
min_rf[0] = refill_costs[0]

for i in range(1, n):
    min_rf[i] = min(min_rf[i - 1], refill_costs[i])

tmp_dist = 0
i = 1
refill_cost = min_rf[0]
ans = 0

for i in range(1, n):
    tmp_dist += moving_costs[i - 1]

    if min_rf[i] < refill_cost:
        ans += tmp_dist * refill_cost
        refill_cost = min_rf[i]
        tmp_dist = 0
    
    if i == n - 1:
        ans += tmp_dist * refill_cost


print(ans)