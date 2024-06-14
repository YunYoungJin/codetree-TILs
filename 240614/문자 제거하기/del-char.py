s = input()
arr = list(s)

while len(arr) != 1:
    n = int(input())
    if n >= len(arr):
        arr.pop()
    else:
        arr.pop(n)
    print(''.join(arr))