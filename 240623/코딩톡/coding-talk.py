n, m, p = map(int, input().split())

talkers = ['A']

for _ in range(n - 1):
    talkers.append(chr(ord(talkers[-1]) + 1))

infos = [
    tuple(input().split())
    for _ in range(m)
]

# p번째 메시지를 보낸 사람, 안 읽은 사람 수
pc, pu = infos[p - 1]
reader_list = []
if int(pu) == 0:
    reader_list = talkers

for c, u in infos:
    if int(u) >= int(pu):
        if c not in reader_list:
            reader_list.append(c)

print(*(set(talkers) - set(reader_list)))