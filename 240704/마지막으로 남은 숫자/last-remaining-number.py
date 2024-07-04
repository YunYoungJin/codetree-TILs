import sys
import heapq

n = int(input())
arr = list(map(int, sys.stdin.readline().split()))
heap = []

for num in arr:
    heapq.heappush(heap, -num)

while len(heap) >= 2:
    first = -heapq.heappop(heap)
    second = - heapq.heappop(heap)

    if first == second:
        continue
    else:
        heapq.heappush(heap, -(first - second))

if heap:
    print(-heap[0])
else:
    print(-1)