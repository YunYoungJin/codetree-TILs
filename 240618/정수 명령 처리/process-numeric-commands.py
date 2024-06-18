class Stack:
    def __init__(self):          # 빈 스택 하나를 생성합니다.
        self.items = []
                
    def push(self, item):        # 스택에 데이터를 추가합니다.
        self.items.append(item)
                
    def empty(self):             # 스택이 비어있으면 True를 반환합니다.
        return not self.items
                
    def size(self):              # 스택에 있는 데이터 수를 반환합니다.
        return len(self.items)
        
    def pop(self):               # 스택의 가장 위에 있는 데이터를 반환하고 제거합니다.
        if self.empty():
            raise Exception("Stack is empty")
            
        return self.items.pop()
                
    def top(self):               # 스택의 가장 위에 있는 데이터를 제거하지 않고 반환합니다.
        if self.empty():
            raise Exception("Stack is empty")
                        
        return self.items[-1]

n = int(input())
stack = Stack()

for _ in range(n):
    s = input().split()

    if s[0] == 'push':
        stack.push(int(s[1]))
    elif s[0] == 'pop':
        print(stack.pop())
    elif s[0] == 'size':
        print(stack.size())
    elif s[0] == 'empty':
        print(1 if stack.empty() else 0)
    else:
        print(stack.top())