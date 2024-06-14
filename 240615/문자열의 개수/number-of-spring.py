arr = []

for _ in range(200):
    s = input()
    if s == '0':
        break
    else:
        arr.append(s)

print(len(arr))
for i in range(len(arr)):
    if i % 2 == 0:
        print(arr[i])