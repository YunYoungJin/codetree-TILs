n = int(input())
s1 = set(list(map(int, input().split())))
m = int(input())
s2 = list(map(int, input().split()))

for item in s2:
    if item in s1:
        print(1, end=' ')
    else:
        print(0, end=' ')