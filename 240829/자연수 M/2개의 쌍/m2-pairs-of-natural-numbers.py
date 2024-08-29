import sys

n = int(input())
arr = []

for _ in range(n):
    x, y = map(int, input().split())
    arr.append((y, x))
arr.sort()  # 정렬

nums = []
counts = []
for y, x in arr:
    nums.append(y)
    counts.append(x)

left = 0
right = len(nums) - 1
c = -sys.maxsize

while left <= right:
    # 최소값과 최대값을 매칭
    current_sum = nums[left] + nums[right]
    c = max(c, current_sum)

    # 두 개 수가 다를 때는 빈도수 더 적은 개수 소모
    min_count = min(counts[left], counts[right])
    if left != right:
        counts[left] -= min_count
        counts[right] -= min_count
    else:
        counts[left] -= min_count

    # 왼쪽 값을 다 소모했다면, 다음으로 이동
    if counts[left] == 0:
        left += 1
    # 오른쪽 값을 다 소모했다면, 다음으로 이동
    if counts[right] == 0:
        right -= 1

print(c)