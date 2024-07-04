from functools import cmp_to_key

def compare(x, y):
    if x + y > y + x:
        return -1
    
    if y + x > x + y:
        return 1
    
    return 0

n = int(input())
arr = [
    input()
    for _ in range(n)
]

arr.sort(key=cmp_to_key(compare))

for elem in arr:
    print(elem, end='')