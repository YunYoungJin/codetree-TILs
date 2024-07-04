n, k = map(int, input().split())
arr = list(map(int, input().split()))
d = dict()

ans = 0

for num in arr:
    complement = k - num
    if complement not in d:
        d[complement] = 0
    else:
        ans += d[complement]

    if num not in d:
        d[num] = 1
    else:
        d[num] += 1

    
print(ans)