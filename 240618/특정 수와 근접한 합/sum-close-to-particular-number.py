import sys
n, s = map(int, input().split())
arr = list(map(int, input().split()))

arr_sum = sum(arr)
min_val = sys.maxsize

for i in range(n):
    for j in range(i + 1, n):
        num = abs(s - (arr_sum - (arr[i] + arr[j])))
        if num < min_val:
            min_val = num
print(min_val)