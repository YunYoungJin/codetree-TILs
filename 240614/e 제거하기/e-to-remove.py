s = input()
arr = list(s)

arr.pop(arr.index('e'))
print("".join(arr))