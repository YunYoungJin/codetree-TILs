import sys

n = int(input())
arr = list(map(int, input().split()))

if n == 2:
    if arr[0] > arr[1]:
        print(arr[0], arr[1])
    else:
        print(arr[1], arr[0])
else:
    max_1st = -sys.maxsize
    max_2nd = -sys.maxsize

    for num in arr:
        if num > max_1st:
            max_2st = max_1st
            max_1st = num
        elif num > max_2nd:
            max_2nd = num
    print(max_1st, max_2nd)