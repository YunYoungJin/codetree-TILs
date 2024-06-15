def cal_pow(a, b):
    return a ** b

n, m = map(int, input().split())
res = cal_pow(n, m)
print(res)