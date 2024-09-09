n, q = map(int, input().split())
colored = set()

for _ in range(q):
    target = int(input())
    current = target
    blocked_node = 0  # 루트에 가장 가까운 색칠된 노드 추적
    
    # 루트로 가는 경로를 확인하며 역순으로 탐색
    while current > 1:
        if current in colored:
            blocked_node = current
        current //= 2
    
    # 도달이 가능한 경우
    if blocked_node == 0:
        colored.add(target)
        print(0)
    else:
        print(blocked_node)