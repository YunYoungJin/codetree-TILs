from sortedcontainers import SortedSet

t = int(input())

for _ in range(t):
    k = int(input())

    s = SortedSet()

    for _ in range(k):
        q, x = input().split()

        if q == 'I':
            s.add(int(x))
        else:
            if len(s) == 0:
                continue
            elif int(x) == 1:
                s.remove(s[-1])
            elif int(x) == -1:
                s.remove(s[0])
    
    if len(s) == 0:
        print("EMPTY")
    else:
        print(s[-1], s[0])