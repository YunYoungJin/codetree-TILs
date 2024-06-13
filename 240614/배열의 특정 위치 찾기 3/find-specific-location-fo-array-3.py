arr = list(map(int, input().split()))
idx = 0
for num in arr:
    if num == 0:
        print(sum(arr[idx-3:idx]))
        break
    idx += 1