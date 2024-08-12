n = int(input())
m = int(input())
arr = list(map(int, input().split()))

d = dict()
ans = 0

for num in arr:
    diff = m - num

    if diff > 0 and diff in d:
        ans += d[diff]
    
    if num not in d:
        d[num] = 1
    else:
        d[num] += 1

print(ans)