import sys

n = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

def max_subarray_sum(arr):
    max_ending_here = max_so_far = arr[0]
    for x in arr[1:]:
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far

def max_rectangle_sum(matrix):
    max_sum = float('-inf')
    
    # 모든 행 쌍을 선택하여 처리
    for top in range(n):
        temp = [0] * n
        for bottom in range(top, n):
            # 행 `top`과 `bottom` 사이의 열 합을 계산
            for col in range(n):
                temp[col] += matrix[bottom][col]
            
            current_max = max_subarray_sum(temp)
            max_sum = max(max_sum, current_max)
    
    return max_sum

print(max_rectangle_sum(grid))