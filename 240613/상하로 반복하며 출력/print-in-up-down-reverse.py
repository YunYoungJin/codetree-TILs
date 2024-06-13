n = int(input())

sum_val = n + 1

for i in range(1, n + 1):
    init = i
    for _ in range(n):
        print(init, end='')
        init = sum_val - init
    print()