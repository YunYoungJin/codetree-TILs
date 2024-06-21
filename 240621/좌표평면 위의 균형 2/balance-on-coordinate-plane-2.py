n = int(input())

m = 101

points = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

for i in range(0, 101, 2):
    for j in range(0, 101, 2):
        m1, m2, m3, m4 = 0, 0, 0, 0

        for x, y in points:
            if x > i and y > j:
                m1 += 1
            elif x < i and y > j:
                m2 += 1
            elif x < i and y < j:
                m3 += 1
            else:
                m4 += 1
        m = min(m, max(m1, m2, m3, m4))

print(m)