from sortedcontainers import SortedSet

n, q = map(int, input().split())
vertices = list(map(int, input().split()))

nums = SortedSet(vertices)

for _ in range(q):
    a, b = map(int, input().split())
    idx_a = nums.bisect_left(a)
    idx_b = nums.bisect_right(b)
    
    if idx_a == len(nums):
        print(0)
    else:
        print(idx_b - idx_a)