n = int(input())
arr = list(map(int, input().split()))

min_val = arr[0]

for num in arr:
    if num < min_val:
        min_val = num
print(min_val, arr.count(min_val))