Y, M, D = map(int, input().split())

def is_leap(y):
    if y % 4 != 0 or (y % 100 == 0 and y % 400 != 0):
        return False
    else:
        return True
        
def last_day_number(m, leap):
    if m == 2:
        if leap:
            return 29
        else:
            return 28
    if m == 4 or m == 6 or m == 9 or m == 11:
        return 30
    
    return 31


def judge_day(y, m, d):
    leap = is_leap(y)

    if m <= 12 and d <= last_day_number(m, leap):
        return True
    
    return False

def get_season(m):
    if 3 <= m and m <= 5:
        return "Spring"
    elif 6 <= m and m <= 8:
        return "Summer"
    elif 9 <= m and m <= 11:
        return "Fall"
    else:
        return "Winter"

if judge_day(Y, M, D):
    print(get_season(M))
else:
    print(-1)