import heapq

n, m = map(int, input().split())
arr = list(map(int, input().split()))

heap = []

for elem in arr:
    heapq.heappush(heap, -elem)

for _ in range(m):
    num = -heapq.heappop(heap)
    heapq.heappush(heap, -(num - 1))

print(-heap[0])