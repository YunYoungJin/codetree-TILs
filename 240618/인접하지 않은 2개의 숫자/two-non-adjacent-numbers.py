n = int(input())
arr = list(map(int, input().split()))

max_val = 0
for i in range(n - 1):
    for j in range(i + 2, n):
        max_val = max(max_val, arr[i] + arr[j])
print(max_val)