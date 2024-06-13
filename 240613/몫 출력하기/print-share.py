cnt = 0 
while True:
    n = int(input())
    if n % 2 == 0:
        print(n//2)
        cnt += 1
    if cnt == 3:
        break