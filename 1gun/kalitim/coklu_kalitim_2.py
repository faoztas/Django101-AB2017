class A:
    def yaz(self):
        print("yaz() : A")

class B(A):
    def yaz(self):
        A.yaz(self)

class C:
    def yaz(self):
        print("yaz() : C")

class D(B, C):
    def yaz(self):
        C.yaz(self)

