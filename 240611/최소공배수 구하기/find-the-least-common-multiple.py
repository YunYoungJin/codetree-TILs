n, m = map(int, input().split())

def gcd(a, b):
    return b if a % b == 0 else gcd(b, a % b)

def lcm(a, b):
    return int(a * b / gcd(a, b))

print(lcm(n, m))