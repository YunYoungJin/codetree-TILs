def add(a, b):
    return int(a) + int(b)
def sub(a, b):
    return int(a) - int(b)
def mul(a, b):
    return int(a) * int(b)
def div(a, b):
    return int(a) // int(b)

a, o ,c = input().split()

if o == '+':
    res = add(a, c)
    print(a, o, c, '=', res)
elif o == '-':
    res = sub(a, c)
    print(a, o, c, '=', res)
elif o == '*':
    res = mul(a, c)
    print(a, o, c, '=', res)
elif o == '/':
    res = div(a, c)
    print(a, o, c, '=', res)
else:
    print("False")