import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def build_tree(preorder, inorder):
    if not preorder or not inorder:
        return None
    
    root_value = preorder[0]
    root_index = inorder.index(root_value)
    
    # 왼쪽 서브트리와 오른쪽 서브트리 분리
    left_inorder = inorder[:root_index]
    right_inorder = inorder[root_index + 1:]
    
    left_preorder = []
    right_preorder = []
    
    for x in preorder[1:]:
        if x in left_inorder:
            left_preorder.append(x)
        if x in right_inorder:
            right_preorder.append(x)

    left_subtree = build_tree(left_preorder, left_inorder)
    right_subtree = build_tree(right_preorder, right_inorder)
    
    return (root_value, left_subtree, right_subtree)

def postorder_traversal(tree):
    if tree is None:
        return []
    
    root_value, left_subtree, right_subtree = tree
    result = []
    result.extend(postorder_traversal(left_subtree))
    result.extend(postorder_traversal(right_subtree))
    result.append(root_value)
    return result


n = int(input())
preorder = list(map(int, input().split()))
inorder = list(map(int, input().split()))

# 트리 구축
tree = build_tree(preorder, inorder)

# 후위 순회
postorder_result = postorder_traversal(tree)

print(*postorder_result)