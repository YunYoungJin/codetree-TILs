base = input()
goal = input()

def find(str1, str2):
    n1 = len(str1)
    n2 = len(str2)

    exists = False

    for i in range(n1 - n2 + 1):
        all_same = True
        for j in range(n2):
            if str1[i + j] != str2[j]:
                all_same = False
        
        if all_same == True:
            exists = True
            return i
    return -1

print(find(base, goal))