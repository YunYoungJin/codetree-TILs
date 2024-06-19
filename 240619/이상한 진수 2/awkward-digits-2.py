a = input()

max_n = 0

for i in range(1, len(a)):
    tmp = ''
    if a[i] == '0':
        tmp = a[:i] + '1' + a[i + 1:]
    else:
        tmp = a[:i] + '0' + a[i + 1:]
    tmp = int(tmp, 2)
    max_n = max(max_n, tmp)
print(max_n)