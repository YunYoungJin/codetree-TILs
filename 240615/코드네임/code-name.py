class spy:
    def __init__(self, codename, score):
        self.codename = codename
        self.score = score

spies = []
for _ in range(5):
    name, score = input().split()
    spies.append(spy(name, int(score)))

low_spy = spies[0]

for spy in spies:
    if spy.score < low_spy.score:
        low_spy = spy

print(f"{low_spy.codename} {low_spy.score}")