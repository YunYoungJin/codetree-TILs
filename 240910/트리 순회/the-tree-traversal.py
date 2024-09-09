n = int(input())
tree = dict()

for _ in range(n):
    parent, left, right = input().split()
    tree[parent] = (left, right)


def preorder(node):
    if node == '.':
        return
    print(node, end='')   # 노드 방문
    preorder(tree[node][0])  # 왼쪽 자식 방문
    preorder(tree[node][1])  # 오른쪽 자식 방문


def inorder(node):
    if node == '.':
        return
    inorder(tree[node][0])  # 왼쪽 자식 방문
    print(node, end='')     # 노드 방문
    inorder(tree[node][1])  # 오른쪽 자식 방문


def postorder(node):
    if node == '.':
        return
    postorder(tree[node][0])  # 왼쪽 자식 방문
    postorder(tree[node][1])  # 오른쪽 자식 방문
    print(node, end='')       # 노드 방문


preorder('A')
print()
inorder('A')
print()
postorder('A')