import sys

n = int(input())
hills = [
    int(input())
    for _ in range(n)
]

min_cost = sys.maxsize

for i in range(0, 84):
    cost = 0
    for hill in hills:
        if i <= hill and hill <= i + 17:
            continue
        elif hill < i:
            cost += (i - hill) ** 2
        elif hill > i + 17:
            cost += (hill - i - 17) ** 2
    
    min_cost = min(min_cost, cost)

print(min_cost)