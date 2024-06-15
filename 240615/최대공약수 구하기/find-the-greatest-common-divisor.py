def print_gcd(a, b):
    while b > 0:
        a, b = b, a % b
    print(a)

n, m = map(int, input().split())
print_gcd(n, m)