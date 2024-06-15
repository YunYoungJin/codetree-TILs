def is_magic_number(n):
    if n % 2 == 0 and (n // 10 + n % 10) % 5 == 0:
        return True
    else:
        return False

n = int(input())

if is_magic_number(n):
    print("Yes")
else:
    print("No")