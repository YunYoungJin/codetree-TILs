arr = []
for _ in range(3):
    arr.append(list(map(int, input().split())))
input()
arr2 = []
for _ in range(3):
    arr2.append(list(map(int, input().split())))

for i in range(3):
    for j in range(3):
        print(arr[i][j] * arr2[i][j], end=' ')
    print()