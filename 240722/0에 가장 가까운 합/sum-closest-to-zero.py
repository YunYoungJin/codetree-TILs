import sys

INT_MAX = sys.maxsize
n = int(input())
arr = list(map(int, input().split()))
arr.sort()

ans = INT_MAX
left = 0
right = n - 1

while left < right:
    current_sum = arr[left] + arr[right]

    if abs(current_sum) < ans:
        ans = current_sum
    
    if current_sum < 0:
        left += 1
    else:
        right -= 1
    
print(ans)