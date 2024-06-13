n = int(input())
c = 65
for _ in range(n):
    for _ in range(n):
        print(chr(c), end='')
        c += 1
    print()