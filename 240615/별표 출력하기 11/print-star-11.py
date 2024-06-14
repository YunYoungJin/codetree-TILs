n = int(input())

for i in range(2 * n + 1): 
    for j in range(2 * n + 1):
        if i % 2 == 1 and j % 2 == 1:
            print(" ", end=" ")
        else:
            print("*", end=" ")
    print()