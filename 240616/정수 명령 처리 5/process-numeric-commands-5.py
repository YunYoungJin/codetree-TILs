n = int(input())
arr = []
for _ in range(n):
    tmp = input().split()
    if tmp[0] == 'push_back':
        arr.append(int(tmp[1]))
    elif tmp[0] == 'pop_back':
        arr.pop()
    elif tmp[0] =='size':
        print(len(arr))
    else:
        print(arr[int(tmp[1])-1])