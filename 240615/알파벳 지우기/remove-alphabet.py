A = input()
B = input()

num1 = ''
num2 = ''

for x in A:
    if x.isdigit():
        num1 += x
for y in B:
    if y.isdigit():
        num2 += y
print(int(num1) + int(num2))