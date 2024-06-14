s = input()
sum_val = 0

for x in s:
    if x.isdigit():
        sum_val += int(x)
print(sum_val)