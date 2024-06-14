s = input()
pivot = s[0]
target = s[1]
arr = list(s)

for i in range(len(arr)):
    if arr[i] == target:
        arr[i] = pivot
print("".join(arr))