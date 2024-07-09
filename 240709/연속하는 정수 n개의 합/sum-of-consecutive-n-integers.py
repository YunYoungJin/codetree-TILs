n, m = map(int, input().split())
arr = list(map(int, input().split()))

sum_val = 0
ans = 0
j = 0

for i in range(n):
    while j < n and sum_val + arr[j] < m:
        sum_val += arr[j]
        j += 1
    
    if j == n:
        break

    if sum_val + arr[j] == m:
        ans += 1
    
    sum_val -= arr[i]

print(ans)