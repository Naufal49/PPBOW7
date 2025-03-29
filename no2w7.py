class Person:
    sehat = False

    def dinyatakan_sehat(self):
        self.sehat = True

joni = Person()
eko = Person()

joni.dinyatakan_sehat()
print("Joni sehat: ", joni.sehat)  # nilai Terbaru
print("Eko sehat: ", eko.sehat)  # nilai default
