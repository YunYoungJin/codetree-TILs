n = int(input())
arr = list(map(int, input().split()))

min_val = 101

for i in range(n - 1):
    if arr[i + 1] - arr[i] < min_val:
        min_val = arr[i + 1] - arr[i]
print(min_val)