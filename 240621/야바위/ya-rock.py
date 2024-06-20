n = int(input())

max_score = 0

orders = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

# 처음 돌을 넣는 컵 
for i in range(3):
    cups = [0] * 3
    cups[i] = 1
    score = 0

    for order in orders:
        a, b, c = order
        cups[a - 1], cups[b - 1] = cups[b -1], cups[a - 1]
        if cups[c - 1] == 1:
            score += 1 
    
    max_score = max(max_score, score)

print(max_score)