m, d = map(int, input().split())

def validation_check(m, d):
    if m >= 13:
        return False
    elif m in [1, 3, 5, 7, 8, 10, 12]:
        if d > 31:
            return False
        else:
            return True
    elif m in [4, 6, 9, 11]:
        if d > 30:
            return False
        else:
            return True
    else:
        if d > 28:
            return False
        else:
            return True

if validation_check(m, d):
    print("Yes")
else:
    print("No")