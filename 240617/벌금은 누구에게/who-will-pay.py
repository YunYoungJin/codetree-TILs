n, m, k = map(int, input().split())
penalty_nums = [0] * n

ans = -1
for _ in range(m):
    who = int(input())
    penalty_nums[who - 1] += 1
    
    if penalty_nums[who - 1] == k:
        ans = who
        break
print(ans)