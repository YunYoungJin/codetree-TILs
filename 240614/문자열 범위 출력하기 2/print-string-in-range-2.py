s = input()
n = int(input())

if n > len(s):
    print(s[::-1])
else:
    for i in range(len(s) - 1, len(s) - 1 - n, -1):
        print(s[i], end='')