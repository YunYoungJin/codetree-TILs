x = int(input())

v = 1
t = 0
s = 0


while True:
    t += 1
    s += v

    if s == x and v == 1:
        break

    remain = x - s

    if ((v + 1) * (v + 2)) / 2 <= remain:
        v += 1
    elif (v * (v + 1)) / 2 <= remain:
        pass    
    elif (v * (v - 1)) / 2 <= remain:
        v -= 1

print(t)