a, b, c = map(int, input().split())
satisfied = True

for i in range(a, b + 1):
    if i % c == 0:
        satisfied = False
if satisfied:
    print("YES")
else:
    print("NO")