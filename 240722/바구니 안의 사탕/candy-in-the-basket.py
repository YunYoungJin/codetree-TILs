n, k = map(int, input().split())
candies = {}

for _ in range(n):
    v, x = map(int, input().split())

    if x not in candies:
        candies[x] = v
    else:
        candies[x] += v

key_list = list(candies.keys())
key_list.sort()

ans = 0
j = 0
tmp_sum = 0

for i in range(len(key_list)):
    while j < n and key_list[j] <= key_list[i] + 2 * k:
        tmp_sum += candies[key_list[j]]
        j += 1
    
    ans = max(ans, tmp_sum)

    tmp_sum -= candies[key_list[i]]

print(ans)