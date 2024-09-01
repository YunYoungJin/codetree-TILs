import sys
import heapq
input = sys.stdin.readline

n, d = map(int, input().split())
points = [
    tuple(map(int, input().split()))
    for _ in range(n)
]
points.sort()

ans = sys.maxsize
left = 0
min_heap = []
max_heap = []
valid = [False] * n

def getMax():
    while max_heap and not valid[max_heap[0][1]]:
        heapq.heappop(max_heap)
    return -max_heap[0][0] if max_heap else 0

def getMin():
    while min_heap and not valid[min_heap[0][1]]:
        heapq.heappop(min_heap)
    return min_heap[0][0] if min_heap else 0

for right in range(n):
    x, y = points[right]
    
    heapq.heappush(min_heap, (y, right))
    heapq.heappush(max_heap, (-y, right))
    valid[right] = True

    while getMax() - getMin() >= d:
        current_range = points[right][0] - points[left][0]
        ans = min(ans, current_range)
        
        valid[left] = False
        left += 1

print(ans if ans != sys.maxsize else -1)