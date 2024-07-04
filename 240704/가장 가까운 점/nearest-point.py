import heapq

n, m = map(int, input().split())
heap = []

for _ in range(n):
    x, y = map(int, input().split())
    heapq.heappush(heap, (x + y, x, y))

for _ in range(m):
    _, x, y = heapq.heappop(heap)
    heapq.heappush(heap, (x + y + 4, x + 2, y + 2))

print(heap[0][1], heap[0][2])