n = int(input())
arr = list(map(int, input().split()))

for item in arr[::-1]:
    if item % 2 == 0:
        print(item, end=' ')