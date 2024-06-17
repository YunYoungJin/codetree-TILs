n, m = map(int, input().split())

pos_A = [0]
pos_B = [0]

for _ in range(n):
    lr, dist = input().split()
    if lr == 'L':
        for _ in range(int(dist)):
            pos_A.append(pos_A[-1] - 1)
    else:
        for _ in range(int(dist)):
            pos_A.append(pos_A[-1] + 1)

for _ in range(m):
    lr, dist = input().split()
    if lr == 'L':
        for _ in range(int(dist)):
            pos_B.append(pos_B[-1] - 1)
    else:
        for _ in range(int(dist)):
            pos_B.append(pos_B[-1] + 1)

meet_time = -1

for i in range(1, len(pos_A)):
    if pos_A[i] == pos_B[i]:
        meet_time = i
        break
print(meet_time)