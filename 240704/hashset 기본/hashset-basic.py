n = int(input())

s = set()

for _ in range(n):
    command = input()

    if command.startswith('add'):
        _, x = command.split()
        s.add(int(x))
    elif command.startswith('remove'):
        _, x = command.split()
        s.remove(int(x))
    else:
        _, x = command.split()
        if int(x) in s:
            print("true")
        else:
            print("false")