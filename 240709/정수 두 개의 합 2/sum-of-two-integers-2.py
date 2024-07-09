n, k = map(int, input().split())
arr = [0]
for _ in range(n):
    arr.append(int(input()))
arr.sort()

ans = 0
j = n

for i in range(1, n + 1):
    while i < j and arr[i] + arr[j] > k:
        j -= 1

    if i == j:
        break
    
    ans += j - i

print(ans)