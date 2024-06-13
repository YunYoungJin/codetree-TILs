count_arr = [0] * 10

arr = list(map(int, input().split()))
for elem in arr:
    if elem == 0:
        break
    else:
        count_arr[elem // 10] += 1

for i in range(1, 10):
    print(f"{i} - {count_arr[i]}")