n, m = map(int, input().split())
uf = list(range(n + 1))

def union(x, y):
  X = find(x)
  Y = find(y)
  uf[X] = Y

def find(x):
  if uf[x] == x:                 # x가 루트 노드라면
    return x                    # x 값을 반환합니다.
  
  root_node = find(uf[x])       # x가 루트 노드가 아니라면, x의 부모인 uf[x]에서 더 탐색을 진행합니다.
  uf[x] = root_node             # 노드 x에 부모를 루트 노드로 설정해줍니다.
  
  return root_node              # 찾아낸 루트 노드를 반환합니다.


for _ in range(m):
    oper, a, b = map(int, input().split())

    if oper == 0:
        union(a, b)
    else:
        if find(a) == find(b):
            print(1)
        else:
            print(0)