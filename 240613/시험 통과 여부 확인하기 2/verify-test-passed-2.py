n = int(input())
cnt = 0
for _ in range(n):
    score = list(map(int, input().split()))
    avg = sum(score)/len(score)
    if avg >= 60:
        print("pass")
        cnt += 1
    else:
        print("fail")
print(cnt)