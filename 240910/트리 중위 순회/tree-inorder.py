k = int(input())
inorder = list(map(int, input().split()))
# 깊이별로 노드 저장
level_nodes = [[] for _ in range(k)]

def build_tree(inorder, depth):
    if not inorder:
        return

    # 중앙 노드가 현재 서브트리의 루트
    mid = len(inorder) // 2
    root = inorder[mid]

    # 현재 깊이에 해당하는 레벨에 루트 추가
    level_nodes[depth].append(root)

    # 서브트리에 대해 재귀 호출
    build_tree(inorder[:mid], depth + 1)  # 왼쪽 서브트리
    build_tree(inorder[mid + 1:], depth + 1)  # 오른쪽 서브트리


# 트리 구축
build_tree(inorder, 0)

# 각 레벨에 저장된 노드들을 출력
for level in level_nodes:
    print(*level)