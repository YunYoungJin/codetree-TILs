s = input()

for x in s:
    if x.isalpha():
        print(x.lower(), end='')
    elif x.isdigit():
        print(x, end='')