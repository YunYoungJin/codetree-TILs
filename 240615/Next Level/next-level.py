class user:
    def __init__(self, Id, Lv):
        self.Id = Id
        self.Lv = Lv

user_a = user("codetree", 10)
Id, level = input().split()
user_b = user(Id, int(level))

print(f"user {user_a.Id} lv {user_a.Lv}")
print(f"user {user_b.Id} lv {user_b.Lv}")