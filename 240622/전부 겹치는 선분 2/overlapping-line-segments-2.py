n = int(input())

segments = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

possible = False

# 제거할 선분 선택
for i in range(n):
    tmp = segments[:i] + segments[i + 1:]

    max_x1 = 0
    min_x2 = 101

    for x1, x2 in tmp:
        max_x1 = max(max_x1, x1)
        min_x2 = min(min_x2, x2)
    

    if min_x2 >= max_x1:
        possible = True
        break

if possible:
    print("Yes")
else:
    print("No")