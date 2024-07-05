import sys

n = int(input())
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))
C = list(map(int, sys.stdin.readline().split()))
D = list(map(int, sys.stdin.readline().split()))

count = dict()
ans = 0

for num1 in A:
    for num2 in B:
        ab = num1 + num2
        if ab not in count:
            count[ab] = 1
        else:
            count[ab] += 1

for num3 in C:
    for num4 in D:
        cd = -(num3 + num4)
        if cd in count:
            ans += count[cd]

print(ans)