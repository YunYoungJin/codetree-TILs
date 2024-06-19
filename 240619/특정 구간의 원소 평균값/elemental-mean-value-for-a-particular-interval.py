n = int(input())
arr = list(map(int, input().split()))

ans = 0
for i in range(n):
    for j in range(i, n):
        sum_val = 0
        tmp = []
        for k in range(i, j + 1):
            tmp.append(arr[k])
        
        avg = sum(tmp) / len(tmp)
        if avg in tmp:
            ans += 1

print(ans)