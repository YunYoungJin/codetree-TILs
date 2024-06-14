n = int(input())
sum_val = 0

for _ in range(n):
    sum_val += int(input())

res = str(sum_val)
print(res[1:] + res[0])