n = int(input())

d = dict()

for _ in range(n):
    command = input()

    if command.startswith('add'):
        _, k, v = command.split()
        d[int(k)] = int(v)
    elif command.startswith('remove'):
        _, k = command.split()
        d.pop(int(k))
    else:
        _, k = command.split()
        if int(k) in d:
            print(d[int(k)])
        else:
            print("None")