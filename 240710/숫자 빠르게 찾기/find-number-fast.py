n, m = map(int, input().split())
arr = list(map(int, input().split()))

for _ in range(m):
    pivot = int(input())

    idx = -1
    left = 0
    right = n - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == pivot:
            idx = mid
            break

        elif arr[mid] > pivot:
            right = mid - 1
        else:
            left = mid + 1
    
    if idx == -1:
        print(-1)
    else:
        print(idx + 1)