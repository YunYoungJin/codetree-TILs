age_sum = 0
cnt = 0
while True:
    age = int(input())
    if 20 <= age and age <= 29:
        age_sum += age
        cnt += 1
    else:
        break
print(f"{age_sum/cnt:.2f}")