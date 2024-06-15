class meeting:
    def __init__(self, sc, mp, t):
        self.sc = sc
        self.mp = mp
        self.t = t

sc, mp, t = input().split()
meet = meeting(sc, mp, t)
print("secret code :", meet.sc)
print("meeting point :", meet.mp)
print("time :", meet.t)