n = int(input())
arr = list(map(int, input().split()))

num_list = sorted(list(set(arr)))

if len(num_list) >= 2:
    second_min = num_list[1]
    if arr.count(second_min) >= 2:
        print(-1)
    else:
        print(arr.index(second_min) + 1)
else:
    print(-1)