n = int(input())
graph = dict()

for i in range(1, n + 1):
    lc, rc = map(int, input().split())
    graph[i] = (lc, rc)

k = int(input())


current_node = 1  # 루트 노드는 1번

# 리프 노드에 도달할 때까지 이동
while True:
    left, right = graph[current_node]
    
    # 리프 노드에 도달한 경우
    if left == -1 and right == -1:
        break
    
    # 왼쪽 자식만 있는 경우
    if right == -1:
        current_node = left
    # 오른쪽 자식만 있는 경우
    elif left == -1:
        current_node = right
    else:
        # 두 자식이 모두 있는 경우
        if k % 2 == 1:
            current_node = left
            k = (k // 2) + 1
        else:
            current_node = right
            k = k // 2

print(current_node)