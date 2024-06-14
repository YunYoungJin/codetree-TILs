n, A = input().split()
cnt = 0

for _ in range(int(n)):
    s = input()
    if s == A:
        cnt += 1
print(cnt)