import heapq

n = int(input())

heap = []

for _ in range(n):
    command = input()

    if command.startswith('push'):
        _, x = command.split()
        heapq.heappush(heap, -int(x))
    elif command.startswith('pop'):
        print(-heapq.heappop(heap))
    elif command.startswith('size'):
        print(len(heap))
    elif command.startswith('empty'):
        print(1 if len(heap) == 0 else 0)
    else:
        print(-heap[0])