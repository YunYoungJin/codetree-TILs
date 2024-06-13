arr = list(map(int, input().split()))

arr2 = []
for num in arr:
    if num == 0:
        break
    else:
        arr2.append(num)

for num in arr2[::-1]:
    print(num, end=' ')