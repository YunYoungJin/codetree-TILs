A = input()

def check_different(string):
    for i in range(len(string)):
        for j in range(i + 1, len(string)):
            if string[i] != string[j]:
                return True
    return False

if check_different(A):
    print("Yes")
else:
    print("No")