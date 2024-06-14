s = input()

for x in s:
    if 'a' <= x and x <= 'z':
        print(x.upper(), end='')
    elif 'A' <= x and x <= 'Z':
        print(x.lower(), end='')