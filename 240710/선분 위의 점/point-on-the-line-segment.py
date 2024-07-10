n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

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


for _ in range(m):
    x1, x2 = map(int, input().split())

    lb = find_lower_bound(x1)
    rb = find_upper_bound(x2)

    print(rb - lb)