n = int(input())
parents = list(map(int, input().split()))
remove_node = int(input())

graph = [[] for _ in range(n)]
root = -1

for child, parent in enumerate(parents):
    if parent == -1:
        root = child
    else:
        graph[parent].append(child)

# 노드 삭제 및 자손 제거
def delete_subtree(graph, node):
    for child in graph[node]:
        delete_subtree(graph, child)
    graph[node] = []  # 해당 노드의 자식 노드 리스트 초기화


# 루트가 삭제될 경우 처리
if remove_node == root:
    root = -1
else:
    # 부모 노드의 자식 리스트에서 삭제할 노드 제거
    for i in range(n):
        if remove_node in graph[i]:
            graph[i].remove(remove_node)
            break
    # 삭제 노드와 자식 노드들 제거
    delete_subtree(graph, remove_node)

# 리프 노드 개수 계산
def count_leaves(graph, root):
    # 삭제된 노드로 인해 트리가 비어 있다면 리프 노드 개수는 0
    if root == -1:
        return 0
    
    # 리프 노드의 개수를 세는 함수
    def dfs(node):
        # 자식이 없는 노드라면 리프 노드로 간주
        if len(graph[node]) == 0:
            return 1

        leaf_count = 0

        for child in graph[node]:
            leaf_count += dfs(child)

        return leaf_count
    
    return dfs(root)

leaf_count = count_leaves(graph, root)
print(leaf_count)