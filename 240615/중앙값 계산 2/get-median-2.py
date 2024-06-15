n = int(input())
arr = list(map(int, input().split()))
sorted_arr = []

for i in range(len(arr)):
    sorted_arr.append(arr[i])
    if i % 2 == 0:
        sorted_arr.sort()
        print(sorted_arr[i // 2], end=' ')