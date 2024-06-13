arr = list(map(int, input().split()))
cnt = 0

for elem in arr:
	if elem == 0:
		break
	cnt += 1

sum_val = 0
for i in range(cnt - 1, -1, -1):
	sum_val += arr[i]
print(f"{sum_val} {sum_val/cnt:.1f}")