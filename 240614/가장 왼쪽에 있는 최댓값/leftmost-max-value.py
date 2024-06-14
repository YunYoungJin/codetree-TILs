n = int(input())
arr = list(map(int, input().split()))

while True:
    max_val = max(arr)
    max_idx = arr.index(max_val)
    print(max_idx + 1, end=' ')
    if max_idx == 0:
        break
    arr = arr[:max_idx]