def is_leap(y):
    if y % 4 != 0 or (y % 100 == 0 and y % 400 != 0):
        return False
    else:
        return True

y = int(input())

if is_leap(y):
    print("true")
else:
    print("false")