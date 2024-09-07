class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self, initial_value):
        self.cur = Node(initial_value)  # 초기 cur 노드 설정

    def insert_before(self, value):
        new_node = Node(value)
        new_node.next = self.cur
        if self.cur.prev:
            new_node.prev = self.cur.prev
            self.cur.prev.next = new_node
        self.cur.prev = new_node

    def insert_after(self, value):
        new_node = Node(value)
        new_node.prev = self.cur
        if self.cur.next:
            new_node.next = self.cur.next
            self.cur.next.prev = new_node
        self.cur.next = new_node

    def move_left(self):
        if self.cur.prev:
            self.cur = self.cur.prev

    def move_right(self):
        if self.cur.next:
            self.cur = self.cur.next

    def print_cur_status(self):
        prev_value = self.cur.prev.value if self.cur.prev else "(Null)"
        cur_value = self.cur.value
        next_value = self.cur.next.value if self.cur.next else "(Null)"
        print(prev_value, cur_value, next_value)


S_init = input().strip()
N = int(input())

dll = DoublyLinkedList(S_init)  # 이중 연결 리스트 생성

# 명령어 처리
for _ in range(N):
    command = input().strip().split()
    if command[0] == '1':  # 노드를 현재 노드 앞에 삽입
        dll.insert_before(command[1])
    elif command[0] == '2':  # 노드를 현재 노드 뒤에 삽입
        dll.insert_after(command[1])
    elif command[0] == '3':  # 현재 노드를 왼쪽으로 이동
        dll.move_left()
    elif command[0] == '4':  # 현재 노드를 오른쪽으로 이동
        dll.move_right()
    
    # 현재 상태 출력
    dll.print_cur_status()