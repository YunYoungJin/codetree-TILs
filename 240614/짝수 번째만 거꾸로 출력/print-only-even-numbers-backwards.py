s = input()

s_even = s[1::2]

for item in s_even[::-1]:
    print(item, end='')