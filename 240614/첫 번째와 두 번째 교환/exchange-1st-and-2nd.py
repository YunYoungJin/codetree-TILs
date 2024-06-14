s = input()
first, second = s[0], s[1]
arr = list(s)

for i in range(len(arr)):
    if arr[i] == first:
        arr[i] = second
    elif arr[i] == second:
        arr[i] = first
print(''.join(arr))