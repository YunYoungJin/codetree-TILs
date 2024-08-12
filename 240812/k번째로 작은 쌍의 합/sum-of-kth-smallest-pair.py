import heapq

n, m, k = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

arr1.sort()
arr2.sort()

# 최소 합을 가지는 쌍 관리
min_heap = []
for i in range(min(n, k)):
    heapq.heappush(min_heap, (arr1[i] + arr2[0], i, 0))

# k번째로 작은 합을 찾기
count = 0
while min_heap:
    sum_value, i, j = heapq.heappop(min_heap)
    count += 1
    if count == k:
        print(sum_value)
        break
    
    # 다음 가능한 쌍을 힙에 추가
    if j + 1 < m:
        heapq.heappush(min_heap, (arr1[i] + arr2[j + 1], i, j + 1))