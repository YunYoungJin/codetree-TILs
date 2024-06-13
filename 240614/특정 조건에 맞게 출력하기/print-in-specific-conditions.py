arr = list(map(int, input().split()))
new_arr = []

for num in arr:
    if num == 0:
        break
    else:
        if num % 2 == 0:
            new_arr.append(num // 2)
        else:
            new_arr.append(num + 3)
print(*new_arr)