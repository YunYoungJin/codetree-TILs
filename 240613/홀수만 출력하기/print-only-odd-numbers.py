N = int(input())

for _ in range(N):
    n = int(input())
    if n % 2 == 1 and n % 3 == 0:
        print(n)