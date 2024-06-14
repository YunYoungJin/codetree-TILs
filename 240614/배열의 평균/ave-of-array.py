arr = []
for _ in range(2):
    arr.append(list(map(int, input().split())))
for i in range(2):
    sum_val = sum(arr[i])
    print(f"{sum_val/len(arr[i]):.1f}", end=' ')
print()

for j in range(4):
    sum_val = arr[0][j] + arr[1][j]
    print(f"{sum_val/len(arr):.1f}", end=' ')
print()

sum_val = sum(arr[0]) + sum(arr[1])
print(f"{sum_val/8:.1f}")