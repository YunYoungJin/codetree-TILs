def is_target_number(n):
    if n % 3 == 0:
        return True
    elif '3' in str(n) or '6' in str(n) or '9' in str(n):
        return True
    else:
        return False

a, b = map(int, input().split())
cnt = 0
for i in range(a, b + 1):
    if is_target_number(i):
        cnt += 1

print(cnt)