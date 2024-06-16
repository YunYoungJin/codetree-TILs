string = input()
def matched(string):
    stack = []
    for item in string:
        if item == '(':
            stack.append(item)
        else:
            if len(stack) == 0:
                return False
            stack.pop()

    if len(stack) != 0:
        return False
    
    return True

if matched(string):
    print("Yes")
else:
    print("No")