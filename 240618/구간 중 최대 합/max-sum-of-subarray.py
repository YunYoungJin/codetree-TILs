n, k = map(int, input().split())
arr = list(map(int, input().split()))

max_sum = 0

for i in range(n - k + 1):
    tmp_sum = 0
    for j in range(i, i + k):
        tmp_sum += arr[j]
    max_sum = max(max_sum, tmp_sum)
print(max_sum)