import sys

n = int(input())
arr = list(map(int, sys.stdin.readline().split()))

if n == 3:
    print(arr[0] * arr[1] * arr[2])
else:
    max_mul = -sys.maxsize
    arr.sort()
    pos_cnt = 0
    neg_cnt = 0

    for num in arr:
        if num > 0 :
            pos_cnt += 1
        elif num < 0:
            neg_cnt += 1

    # 양수가 없을 때
    if pos_cnt == 0:
        max_mul = max(max_mul, arr[-1] * arr[-2] * arr[-3])
    
    # 양수가 있을 때
    # (+--)거나 (+++)일 때 최대 
    else:
        max_mul = max(arr[-1] * arr[-2] * arr[-3], arr[-1] * arr[0] * arr[1])

print(max_mul)