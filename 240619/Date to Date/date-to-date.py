m1, d1, m2, d2 = map(int, input().split())

num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

a = 0
for i in range(1, m1):
    a += num_of_days[i]
a += d1

b = 0
for j in range(1, m2):
    b += num_of_days[j]
b += d2

print(b - a + 1)