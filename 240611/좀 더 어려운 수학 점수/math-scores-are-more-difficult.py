m1, e1 = map(int, input().split())
m2, e2 = map(int, input().split())

if m1 > m2:
    print("A")
elif m1 < m2:
    print("B")
else:
    if e1 > e2:
        print("A")
    else:
        print("B")