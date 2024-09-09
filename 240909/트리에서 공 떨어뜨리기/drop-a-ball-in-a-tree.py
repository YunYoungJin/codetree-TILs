n = int(input())
graph = dict()

for i in range(1, n + 1):
    lc, rc = map(int, input().split())
    graph[i] = (lc, rc)

k = int(input())

def count_subtree_balls(node, graph, ball_count):
    if node == -1:
        return 0
    left, right = graph[node]

    return ball_count[left] + ball_count[right] + \
        count_subtree_balls(left, graph, ball_count) + \
        count_subtree_balls(right, graph, ball_count)

ball_count = [0] * (n + 1)
ans = 0

# k번의 공을 떨어뜨리는 과정을 시뮬레이션
for i in range(k):
    current_node = 1  # 루트 노드는 항상 1번
    
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
            left_subtree_cnt = count_subtree_balls(left, graph, ball_count)
            right_subtree_cnt = count_subtree_balls(right, graph, ball_count)
            if left_subtree_cnt <= right_subtree_cnt:
                current_node = left
            else:
                current_node = right
    
    # 리프 노드에서 공이 멈춤
    ball_count[current_node] += 1

    if i == k - 1:
        ans = current_node

print(ans)