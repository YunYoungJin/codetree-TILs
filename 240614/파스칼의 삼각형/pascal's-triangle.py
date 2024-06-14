n = int(input())

arr = [
    [0 for _ in range(i + 1)]
    for i in range(n)
]

for i in range(0, n):
    for j in range(0, i+1):
        if i == 0 or j == 0 or j == i:
            arr[i][j] = 1
        else:
            arr[i][j] = arr[i-1][j-1] + arr[i-1][j]

for row in arr:
    for elem in row:
        print(elem, end=" ")
    print()