n = int(input())

students = []
for _ in range(5):
    name, h, w = input().split()
    students.append((name, int(h), int(w)))

students.sort(key = lambda x: (x[1], -x[2]))

for name, h, w in students:
    print(name, h, w)