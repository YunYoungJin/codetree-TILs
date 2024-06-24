s = input()

def check_palindrome(string):
    if string == string[::-1]:
        return True
    else:
        return False

if check_palindrome(s):
    print("Yes")
else:
    print("No")