n = int(input())

for i in range(n):
    if i == 0 or i == n - 1:
        for _ in range(n):
            print("*", end = " ")
    else:
        for j in range(n):
            if j == 0 or j == n - 1:
                print("*", end = " ")
            elif i > j:
                print("*", end = " ")
            else:
                print(" ", end = " ")
    print()