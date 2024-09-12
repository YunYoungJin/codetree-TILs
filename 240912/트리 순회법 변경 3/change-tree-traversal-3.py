import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))
inorder_index = {value: idx for idx, value in enumerate(inorder)}

preorder = []

def in_post_to_pre(post_start, post_end, in_start, in_end):
    if post_start > post_end or in_start > in_end:
        return
    root = postorder[post_end]
    root_idx = inorder_index[root]

    left = root_idx - in_start # 좌측 서브트리 노드 개수
    right = in_end - root_idx # 우측 서브트리 노드 개수
    preorder.append(root)
    in_post_to_pre(post_start, post_start + left - 1, in_start, in_start + left - 1)
    in_post_to_pre(post_end - right, post_end - 1, in_end - right + 1, in_end)

in_post_to_pre(0, n - 1, 0, n - 1)
print(*preorder)