sum_val, cnt = 0, 0

for _ in range(10):
    n = int(input())
    if 0 <= n and n <= 200:
        sum_val += n
        cnt += 1
print(f"{sum_val} {sum_val/cnt:.1f}")