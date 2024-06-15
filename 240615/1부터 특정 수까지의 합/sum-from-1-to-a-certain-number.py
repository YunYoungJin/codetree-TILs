def f(n):
    sum_val = 0
    for i in range(1, n + 1):
        sum_val += i
    return sum_val // 10

n = int(input())
div_num = f(n)
print(div_num)