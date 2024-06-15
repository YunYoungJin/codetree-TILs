a, b = map(int, input().split())

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def is_match(n):
    val = 0
    for i in str(n):
        val += int(i)
    if val % 2 == 0:
        return True
    else:
        return False

cnt = 0

for i in range(a, b + 1):
    if is_prime(i) and is_match(i):
        cnt += 1
print(cnt)