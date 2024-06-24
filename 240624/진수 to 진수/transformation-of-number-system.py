a, b = map(int, input().split())
n = list(input())

num = 0

for i in range(len(n)):
    num = num * a + int(n[i])

digits = []

while True:
    if num < b:
        digits.append(num)
        break

    digits.append(num % b)
    num //= b

# print binary number
for digit in digits[::-1]:
    print(digit, end="")