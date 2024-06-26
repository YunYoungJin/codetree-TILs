n, m = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

gold = 0

for k in range(n + 1):
    cost = k * k + (k + 1) * (k + 1)

    # 중심점 위치
    for i in range(n):
        for j in range(n):
            tmp_gold = 0

            for p in range(-k, k + 1):
                for q in range(-k, k + 1):
                    if k < abs(p) + abs(q):
                        continue
                    
                    if i + p < 0 or n <= i + p:
                        continue

                    if j + q < 0 or n <= j + q:
                        continue
 
                    if grid[i + p][j + q] == 1:
                        tmp_gold += 1
            
            if tmp_gold * m >= cost:
                gold = max(gold, tmp_gold)

                    
print(gold)