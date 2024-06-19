class Product:
    def __init__(self, name, code):
        self.name = name
        self.code = code

name, code = input().split()
pa = Product("codetree", 50)
pb = Product(name, int(code))

print(f"product {pa.code} is {pa.name}")
print(f"product {pb.code} is {pb.name}")