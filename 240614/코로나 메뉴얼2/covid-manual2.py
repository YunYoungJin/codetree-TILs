emer = [0] * 4

for _ in range(3):
    cold, temp = input().split()
    if cold == 'Y':
        if int(temp) >= 37:
            emer[0] += 1
        else:
            emer[2] += 1
    else:
        if int(temp) >= 37:
            emer[1] += 1
        else:
            emer[3] += 1

for item in emer:
    print(item, end=' ')
if emer[0] >= 2:
    print("E")