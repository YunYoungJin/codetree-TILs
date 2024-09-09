n, q = map(int, input().split())
tree = list(range(n + 1))
colored = [0] * (n + 1)

def is_possible(target, current_node):
    if current_node == 1:
        print(0)
        colored[target] = 1
        return
    
    if colored[current_node] == 1:
        print(current_node)
        return
    
    return is_possible(target, current_node // 2)


for _ in range(q):
    target = int(input())
    is_possible(target, target)