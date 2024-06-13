arr = list(map(int, input().split()))

arr2 = []
for num in arr:
    if num >= 250:
        break
    else:
        arr2.append(num)
print(sum(arr2), "%.1f" % (sum(arr2)/len(arr2)))