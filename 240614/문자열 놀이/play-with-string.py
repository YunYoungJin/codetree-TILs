s, q = input().split()
arr = list(s)

for _ in range(int(q)):
    i, a, b = input().split()
    if int(i) == 1:
        arr[int(a)-1], arr[int(b)-1] = arr[int(b)-1], arr[int(a)-1]
    elif int(i) == 2:
        for i in range(len(arr)):
            if arr[i] == a:
                arr[i] = b
    print(''.join(arr))