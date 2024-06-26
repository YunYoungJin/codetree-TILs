n = int(input())
blocks = [ int(input()) for _ in range(n) ]
ses = [ tuple(map(int, input().split())) for _ in range(2) ]

for s, e in ses:
    temp = []
    for i in range(len(blocks)):
        if s - 1 <= i and i <= e - 1:
            continue
        temp.append(blocks[i])
    blocks = temp

print(len(blocks))

if len(blocks) != 0:
    for block in blocks:
        print(block)