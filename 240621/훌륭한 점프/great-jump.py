n, k = map(int, input().split())
arr = list(map(int, input().split()))

def is_possible(max_val):
    available_indices = []
    for i, elem in enumerate(arr):
        if elem <= max_val:
            available_indices.append(i)

    arr_size = len(available_indices)
    for i in range(1, arr_size):
        dist = available_indices[i] - available_indices[i - 1]
        if dist > k:
            return False

    return True

min_of_max = 101
for a in range(100, max(arr[0], arr[-1]) - 1, -1):
    if is_possible(a):
        min_of_max = min(min_of_max, a)

print(min_of_max)