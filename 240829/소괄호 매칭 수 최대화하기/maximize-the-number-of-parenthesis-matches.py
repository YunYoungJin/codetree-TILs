import sys
from functools import cmp_to_key
input = sys.stdin.readline

n = int(input())
sources = []
ans = 0

def check(a, b):
    sum1 = a[0] * b[1]
    sum2 = b[0] * a[1]
    if sum1 > sum2:
        return -1
    else:
        return 1

for _ in range(n):
    s = input().strip()
    open_count = 0
    close_count = 0
    
    for char in s:
        if char == '(':
            open_count += 1
        else:
            close_count += 1
            ans += open_count
    
    sources.append((open_count, close_count))

sources.sort(key=lambda x: (x[1] - x[0]))
sources.sort(key=cmp_to_key(check))

open_sum = 0
for open_count, close_count in sources:
    ans += open_sum * close_count
    open_sum += open_count

print(ans)