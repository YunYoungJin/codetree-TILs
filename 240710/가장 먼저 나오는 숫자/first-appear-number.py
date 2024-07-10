n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = list(map(int, input().split()))

def find_lower_bound(x):
    left = 0
    right = n - 1
    min_idx = n

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] >= x:
            min_idx = min(min_idx, mid)
            right = mid - 1
        else:
            left = mid + 1
    
    return min_idx


def find_upper_bound(x):
    left = 0
    right = n - 1
    min_idx = n

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] > x:
            min_idx = min(min_idx, mid)
            right = mid - 1
        else:
            left = mid + 1
    
    return min_idx


for num in queries:
    if num < arr[0] or num > arr[-1]:
        print(-1)
        continue

    lb = find_lower_bound(num)
    rb = find_upper_bound(num)

    if lb == rb:
        print(-1)
    else:
        print(lb + 1)