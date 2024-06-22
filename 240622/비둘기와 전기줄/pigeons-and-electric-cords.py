n = int(input())

infos = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

pg_pos = [-1] * 11

move = 0

for pg_num, pos in infos:
    if pg_pos[pg_num] == -1:
        pg_pos[pg_num] = pos
    elif pg_pos[pg_num] != pos:
        move += 1

print(move)