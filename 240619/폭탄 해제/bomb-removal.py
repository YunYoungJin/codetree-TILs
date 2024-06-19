class bomb:
    def __init__(self, code, color, second):
        self.code = code
        self.color = color
        self.second = second

code, color, second = input().split()
bomb_A = bomb(code, color, int(second))

print(f"code : {bomb_A.code}")
print(f"color : {bomb_A.color}")
print(f"second : {bomb_A.second}")