from sortedcontainers import SortedDict

n = int(input())
sd = SortedDict()

for _ in range(n):
    command = input()

    if command.startswith('add'):
        _, k, v = command.split()
        sd[int(k)] = int(v)
    elif command.startswith('remove'):
        _, k = command.split()
        sd.pop(int(k))
    elif command.startswith('find'):
        _, k = command.split()
        print(sd.get(int(k)))
    else:
        if len(sd) == 0:
            print("None")
        else:
            for key, value in sd.items():
                print(value, end=' ')
            print()