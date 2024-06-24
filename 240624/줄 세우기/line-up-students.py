n = int(input())

students = [
    [i + 1] + list(map(int, input().split()))
    for i in range(n)
]

students.sort(key = lambda x: (-x[1], -x[2], x[0]))

for no, h, w in students:
    print(h, w, no)