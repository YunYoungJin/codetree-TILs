import heapq

n = int(input())
arr = list(map(int, input().split()))

heap = []

for num in arr:
    heapq.heappush(heap, num)

    if len(heap) < 3:
        print(-1)
    else:
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        print(a * b * heap[0])
        heapq.heappush(heap, a)
        heapq.heappush(heap, b)