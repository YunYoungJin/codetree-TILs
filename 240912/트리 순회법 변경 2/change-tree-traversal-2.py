import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

n = int(input())
preorder = list(map(int, input().split()))
inorder = list(map(int, input().split()))
inorder_index = {value: idx for idx, value in enumerate(inorder)}

postorder = []

def pre_in_to_post(pre_start, pre_end, in_start, in_end):
    if pre_start > pre_end or in_start > in_end:
        return
    root = preorder[pre_start]
    root_idx = inorder_index[root]

    left = root_idx - in_start # 좌측 서브트리 노드 개수
    right = in_end - root_idx # 우측 서브트리 노드 개수
    pre_in_to_post(pre_start + 1, pre_start + left, in_start, in_start + left - 1)
    pre_in_to_post(pre_end - right + 1, pre_end, in_end - right + 1, in_end)
    postorder.append(root)

pre_in_to_post(0, n - 1, 0, n - 1)
print(*postorder)