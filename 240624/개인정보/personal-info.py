students = []
for _ in range(5):
    name, h, w = input().split()
    students.append((name, int(h), float(w)))

students.sort(key = lambda x: x[0])

print("name")
for name, h, w in students:
    print(f"{name} {h} {w:.1f}")

students.sort(key = lambda x: -x[1])

print("\nheight")
for name, h, w in students:
    print(f"{name} {h} {w:.1f}")