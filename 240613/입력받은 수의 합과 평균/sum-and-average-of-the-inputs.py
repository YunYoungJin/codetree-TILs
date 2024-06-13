n = int(input())
sum_val = 0
for _ in range(n):
    num = int(input())
    sum_val += num
print(f"{sum_val} {sum_val/n:.1f}")