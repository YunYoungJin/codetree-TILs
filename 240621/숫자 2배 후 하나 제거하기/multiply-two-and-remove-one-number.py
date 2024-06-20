import sys

n = int(input())

arr = list(map(int, input().split()))

min_diff = sys.maxsize

# 2배 곱할 원소 선택
for i in range(n):
    arr[i] *= 2

    # 제외할 원소 선택
    for j in range(n):
        remain = []
        
        for k, num in enumerate(arr):
            if k != j:
                remain.append(num)
        
        sum_diff = 0
        
        for l in range(n - 2):
            sum_diff += abs(remain[l + 1] - remain[l])

        min_diff = min(min_diff, sum_diff)

    arr[i] //= 2

print(min_diff)