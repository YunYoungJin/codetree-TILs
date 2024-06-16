n = int(input())
arr = list(map(int, input().split()))

pos = 1

while True:
    arr_new = [[] for _ in range(10)]
    for i in range(len(arr)):
        digit = (arr[i] % (10 * pos)) // pos
        arr_new[digit].append(arr[i])

    if len(arr_new[0]) == len(arr):
        break

    store_arr = []
    for i in range(10):
        for j in arr_new[i]:
            store_arr.append(j)

    arr = store_arr
    pos *= 10

print(*arr)