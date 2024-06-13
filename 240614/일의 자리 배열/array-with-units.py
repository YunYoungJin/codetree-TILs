a, b = map(int, input().split())

for i in range(10):
    print(a % 10, end=' ')
    a, b = b, a + b