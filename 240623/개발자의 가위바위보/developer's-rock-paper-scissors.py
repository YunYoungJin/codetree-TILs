n = int(input())

results = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

rsps = [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
max_win_a = 0

for r, s, p in rsps:
    tmp_win_a = 0
    a_win_cases = [(r, s), (s, p), (p, r)]
    
    for result in results:
        if result in a_win_cases:
            tmp_win_a += 1
    
    max_win_a = max(max_win_a, tmp_win_a)

print(max_win_a)