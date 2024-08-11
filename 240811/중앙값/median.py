import heapq

t = int(input())

for _ in range(t):
    m = int(input())
    arr = list(map(int, input().split()))
    max_heap = []  # 중앙값 이하의 값들을 저장
    min_heap = []  # 중앙값 이상의 값들을 저장
    medians = []

    for i, num in enumerate(arr):
        if len(max_heap) == len(min_heap):
            heapq.heappush(max_heap, -num)
        else:
            heapq.heappush(min_heap, num)

        if min_heap and -max_heap[0] > min_heap[0]:
            # 두 힙의 균형을 맞추기 위해 값을 교환
            to_min = -heapq.heappop(max_heap)
            to_max = heapq.heappop(min_heap)
            heapq.heappush(max_heap, -to_max)
            heapq.heappush(min_heap, to_min)

        if i % 2 == 0:  # 홀수 번째 원소일 때
            medians.append(-max_heap[0])
    
    print(*medians)