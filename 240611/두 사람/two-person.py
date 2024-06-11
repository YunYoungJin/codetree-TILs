age1, sex1 = input().split()
age2, sex2 = input().split()

if (int(age1) >= 19 and sex1 == 'M') or (int(age2) >= 19 and sex2 == 'M'):
    print(1)
else:
    print(0)