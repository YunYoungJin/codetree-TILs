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

# p번째 메시지를 포함한 이후 메시지를 보낸 사람들은
# 메세지를 확실히 읽었다
reader_list = []
if int(pu) == 0:
    reader_list = talkers
else:
    reader_list.append(pc)

if p >= 2 and pu == infos[p - 2][1]:
    if infos[p - 2][0] not in reader_list:
        reader_list.append(infos[p - 2][0])

for idx in range(p, m):
    c, u = infos[idx]
    if c not in reader_list:
        reader_list.append(c)

print(*(set(talkers) - set(reader_list)))