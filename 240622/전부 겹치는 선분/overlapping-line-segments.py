n = int(input())

segments = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

exist = True

for i in range(n):
    for j in range(i + 1, n):
        x1, x2 = segments[i]
        x3, x4 = segments[j]

        if x2 < x3 or x4 < x1:
            exist = False
            break

if exist:
    print("Yes")
else:
    print("No")