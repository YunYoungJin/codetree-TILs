n = int(input())
arr = [1]
arr.append(n)

while True:
    if arr[-1] + arr[-2] > 100:
        arr.append(arr[-1] + arr[-2])
        break
    arr.append(arr[-1] + arr[-2])
print(*arr)