n = int(input())
arr = list(map(int, input().split()))

arr.sort()
min_max = 0
for i in range(n):
    if min_max < arr[i] + arr[2 * n - i - 1]:
        min_max = arr[i] + arr[2 * n - i - 1]
print(min_max)