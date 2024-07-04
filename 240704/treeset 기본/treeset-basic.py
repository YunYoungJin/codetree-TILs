from sortedcontainers import SortedSet

n = int(input())

s = SortedSet()

for _ in range(n):
    command = input()

    if command.startswith('add'):
        _, x = command.split()
        s.add(int(x))
    elif command.startswith('remove'):
        _, x = command.split()
        s.remove(int(x))
    elif command.startswith('find'):
        _, x = command.split()
        if int(x) in s:
            print("true")
        else:
            print("false")
    elif command.startswith('lower'):
        _, x = command.split()
        if s.bisect_left(int(x)) < len(s):
            print(s[s.bisect_left(int(x))])
        else:
            print("None")
    elif command.startswith('upper'):
        _, x = command.split()
        if s.bisect_right(int(x)) < len(s):
            print(s[s.bisect_right(int(x))])
        else:
            print("None")
    elif command.startswith('largest'):
        if len(s) == 0:
            print("None")
        else:
            print(s[-1])
    else:
        if len(s) == 0:
            print("None")
        else:
            print(s[0])