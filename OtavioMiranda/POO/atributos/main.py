
class A:
    vc = 123

a1 = A()
a2 = A()

a1.vc = 321

print(a1.vc)
print(a2.vc)
print(a1.__dict__)
print(a2.__dict__)

print("###")
class B:
    vc = 123

    def __init__(self):
        self.vc = 321

b1 = B()

print(b1.vc)
print(B.vc)
print(b1.__dict__)
print(B.__dict__)