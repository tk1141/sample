#! python3

class Base:
    basevalue = "base"

    def spam(self):
        print("Base.spam()")

    def ham(self):
        print("ham")


class Derived(Base):
    def spam(self):
        print("Derived.spam()")
        self.ham()


base1 = Base()
base1.spam()
base1.ham()

derived1 = Derived()
derived1.spam()
