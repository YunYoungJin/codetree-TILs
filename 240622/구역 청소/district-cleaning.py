a, b = map(int, input().split())
c, d = map(int, input().split())

if b < c or d < a:
    print(d - c + b - a)
else:
    print(max(b, d) - min(a, c))