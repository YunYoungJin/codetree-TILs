n, q = map(int, input().split())
arr = list(map(int, input().split()))

for _ in range(q):
    tmp = list(map(int, input().split()))
    if tmp[0] == 1:
        print(arr[tmp[1] - 1])
    elif tmp[0] == 2:
        if tmp[1] in arr:
            print(arr.index(tmp[1]) + 1)
        else:
            print(0)
    elif tmp[0] == 3:
        for i in range(tmp[1] - 1, tmp[2]):
            print(arr[i], end=' ')
        print()