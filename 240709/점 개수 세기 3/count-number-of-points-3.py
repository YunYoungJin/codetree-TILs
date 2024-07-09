from sortedcontainers import SortedSet

n, q = map(int, input().split())
vertices = list(map(int, input().split()))

nums = SortedSet(vertices)

for _ in range(q):
    a, b = map(int, input().split())
    idx_a = nums.bisect_left(a)
    idx_b = nums.bisect_left(b)
    
    print(idx_b - idx_a + 1)