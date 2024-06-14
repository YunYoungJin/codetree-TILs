n = int(input())
s = "".join(input().split())

cnt = 0
for i in s:
    print(i, end='')
    cnt +=1 
    if cnt == 5:
        print()
        cnt = 0