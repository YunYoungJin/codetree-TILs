sum_val = 0
n = int(input())
for i in range(1, n):
    if n % i == 0:
        sum_val += i
if n == sum_val:
    print("P")
else:
    print("N")