class Person:
    def __init__(self, name, addr, city):
        self.name = name
        self.addr = addr
        self.city = city

n = int(input())
persons = []

for _ in range(n):
    name, addr, city = input().split()
    person = Person(name, addr, city)
    persons.append(person)

persons.sort(key = lambda x : x.name)

print(f"name {persons[-1].name}")
print(f"addr {persons[-1].addr}")
print(f"city {persons[-1].city}")