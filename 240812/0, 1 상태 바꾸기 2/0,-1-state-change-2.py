n = int(input())
arr = list(map(int, input().split()))
m = int(input())
opers = [
    tuple(map(int, input().split()))
    for _ in range(m)
]

for oper in opers:
    oper_type, num = oper
    if oper_type == 1:
        for i in range(n):
            if (i + 1) % num == 0:
                arr[i] = 1 - arr[i]
    else:
        left = num - 1
        right = num - 1
        
        while left > 0 and right < n - 1 and arr[left - 1] == arr[right + 1]:
            left -= 1
            right += 1
        
        for i in range(left, right + 1):
            arr[i] = 1 - arr[i]

print(*arr)