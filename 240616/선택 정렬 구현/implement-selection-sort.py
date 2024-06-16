n = int(input())
arr = list(map(int, input().split()))

for i in range(n - 1):
    idx = i
    for j in range(i + 1, n):
      if arr[j] < arr[idx]:
        idx = j
    tmp = arr[i]
    arr[i] = arr[idx]
    arr[idx] = tmp
  
print(*arr)