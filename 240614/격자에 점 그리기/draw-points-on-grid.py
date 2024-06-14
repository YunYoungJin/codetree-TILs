n, m = map(int, input().split())

placed = [
   [0 for _ in range(n)]
   for _ in range(n)
]

for i in range(1, m + 1):
   r, c = tuple(map(int, input().split()))
   placed[r - 1][c - 1] = i


for row in placed:
    for elem in row:
        print(elem, end=" ")
    print()