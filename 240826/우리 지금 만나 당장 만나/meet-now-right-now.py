import sys

n = int(input())
xs = list(map(int, input().split()))
vs = list(map(int, input().split()))

def is_possible(time_limit):
    min_pos = -sys.maxsize
    max_pos = sys.maxsize
    
    for x, v in zip(xs, vs):
        left_bound = x - time_limit * v
        right_bound = x + time_limit * v
        
        min_pos = max(min_pos, left_bound)
        max_pos = min(max_pos, right_bound)
        
        if min_pos > max_pos:
            return False
    
    return True

left = 0.0
right = 1000000000.00000

for _ in range(100):
    mid = (left + right) / 2
    
    if is_possible(mid):
        right = mid
    else:
        left = mid

print(f"{left:.4f}")