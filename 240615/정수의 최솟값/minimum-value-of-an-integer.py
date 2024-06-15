def find_min(a, b, c):
    minimum = a
    if b < minimum:
        minimum=b
    if c < minimum:
        minimum=c
    return minimum

a, b, c = map(int, input().split())
print(find_min(a, b, c))