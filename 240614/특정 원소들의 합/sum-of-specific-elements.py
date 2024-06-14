arr = []
for _ in range(4):
    arr.append(list(map(int, input().split())))

sum_val = 0
for i in range(4):
    for j in range(i + 1):
        sum_val += arr[i][j]
print(sum_val)