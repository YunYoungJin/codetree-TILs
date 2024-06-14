import sys

n = int(input())
arr = list(map(int, input().split()))

max_1st = -sys.maxsize
max_2nd = -sys.maxsize

for num in arr:
    if num > max_1st:
        max_2nd = max_1st
        max_1st = num
    elif num > max_2nd:
        max_2nd = num
print(max_1st, max_2nd)