string = input()
stack = []
for item in string:
    if item == '(':
        stack.append(item)
    else:
        if len(stack) == 0:
            print("No")
            break
        stack.pop()

if len(stack) != 0:
    print("No")
else:
    print("Yes")