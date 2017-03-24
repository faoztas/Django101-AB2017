class A:
    def yaz(self):
        print("yaz() : A")

class B(A):
    def yaz(self):
        super(B,self).yaz()

class C:
    def yaz(self):
        print("yaz() : C")

class D(B, C):
    def yaz(self):
        super(D, self).yaz()

