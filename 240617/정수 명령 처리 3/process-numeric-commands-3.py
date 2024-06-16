from collections import deque

dq = deque()

n = int(input())
for _ in range(n):
    s = input().split()
    if s[0] == 'push_front':
        dq.appendleft(int(s[1]))
    elif s[0] == 'push_back':
        dq.append(int(s[1]))
    elif s[0] == 'pop_front':
        print(dq.popleft())
    elif s[0] == 'pop_back':
        print(dq.pop())
    elif s[0] == 'size':
        print(len(dq))
    elif s[0] == 'empty':
        if len(dq) == 0:
            print(1)
        else:
            print(0)
    elif s[0] == 'front':
        print(dq[0])
    else:
        print(dq[-1])