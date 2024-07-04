n = int(input())
arr = list(map(int, input().split()))

tmp_sum = 0

for i in range(n):
    if tmp_sum < 0:
        tmp_sum = arr[i]
    else:
        tmp_sum += arr[i]
print(tmp_sum)