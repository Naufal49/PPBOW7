def add_jutsu(cls):
    def jutsu(self):
        print(f"{self.__class__.__name__}: Rasengan!!!")
    
    cls.jutsu = jutsu
    return cls

@add_jutsu
class Naruto:
    pass

@add_jutsu
class Sasuke:
    def jutsu(self):
        print(f"{self.__class__.__name__}: Chidori!!!")

naruto = Naruto()
sasuke = Sasuke()

naruto.jutsu()  
sasuke.jutsu()  