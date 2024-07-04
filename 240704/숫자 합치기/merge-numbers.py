import heapq

n = int(input())
arr = list(map(int, input().split()))
heap = []

for num in arr:
    heapq.heappush(heap, num)

ans = 0

while len(heap) != 1:
    first = heapq.heappop(heap)
    second = heapq.heappop(heap)
    new_num = first + second
    ans += new_num
    heapq.heappush(heap, new_num)

print(ans)