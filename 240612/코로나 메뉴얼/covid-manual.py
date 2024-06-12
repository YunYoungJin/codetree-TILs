emer = 0

for _ in range(3):
    cold, temp = input().split()
    temp = int(temp)
    if cold == 'Y' and temp >= 37:
        emer += 1

if emer >= 2:
    print("E")
else:
    print("N")