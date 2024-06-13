arr = list(map(int, input().split()))
filtered_arr = arr[1::2]
filtered_arr2 = arr[2::3]

print(sum(filtered_arr), end=' ')
print(f"{sum(filtered_arr2)/len(filtered_arr2):.1f}")