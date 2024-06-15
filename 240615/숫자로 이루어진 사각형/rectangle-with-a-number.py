def print_square(n):
    num = 1
    for _ in range(n):
        for _ in range(n):
            print(num, end=' ')
            num += 1
            if num == 10:
                num = 1
        print()

row_num = int(input())
print_square(row_num)