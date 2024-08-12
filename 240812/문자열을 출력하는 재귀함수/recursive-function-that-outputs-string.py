n = int(input())

def Print(cnt):
    if cnt == 0:
        return

    print("Coding is my favorite hobby!")
    return Print(cnt - 1)

Print(n)