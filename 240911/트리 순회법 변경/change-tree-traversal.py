import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

def build_bst(preorder):
    if not preorder:
        return None
    
    root = preorder[0]
    right_start = len(preorder)

    # 오른쪽 서브트리 시작 인덱스 구하기
    for i in range(1, len(preorder)):
        if preorder[i] > root:
            right_start = i
            break
    
    left_subtree = preorder[1:right_start]
    right_subtree = preorder[right_start:]

    # 서브트리들로 재귀적으로 bst 빌드
    left_tree = build_bst(left_subtree)
    right_tree = build_bst(right_subtree)
    
    return (root, left_tree, right_tree)

def postorder_traversal(tree):
    if tree is None:
        return []
    
    root, left_tree, right_tree = tree

    return postorder_traversal(left_tree) + postorder_traversal(right_tree) + [root]


n = int(input())
preorder = [
    int(input())
    for _ in range(n)
]

bst = build_bst(preorder)
result = postorder_traversal(bst)

for value in result:
    print(value)