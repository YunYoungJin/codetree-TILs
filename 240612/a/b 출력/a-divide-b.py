a, b = map(int, input().split())

for i in range(21):
    if i == 0:
        p = a // b
        a = a % b
        print(p, end='.')
    else:
        p = (a * 10) // b
        a = (a * 10) % b
        print(p, end='')