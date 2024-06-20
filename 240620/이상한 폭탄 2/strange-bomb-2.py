n, k = map(int, input().split())

bomb = [
    int(input())
    for _ in range(n)
]

num = -1

for i in range(n):
    tmp = bomb[i]
    for j in range(i + 1, n):
        if j - i > k:
            break
        if tmp == bomb[j]:
            num = max(num, tmp)
        
print(num)