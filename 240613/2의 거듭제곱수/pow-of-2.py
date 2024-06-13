N = int(input())
prod = 1
x = 0
while True:
    prod *= 2
    x += 1
    if N == prod:
        break
print(x)