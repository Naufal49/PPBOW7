class Passenger:
    TITLES = ("Mr", "Mrs", "Ms")  

    def __init__(self, title, fname, lname):
        if title not in self.TITLES:
            raise ValueError(f"{title} is not a valid title.")

        self.title = title
        self.fname = fname
        self.lname = lname

# Membuat objek Passenger
p1 = Passenger("Mr", "Kiewlamphone", "Souvanlith")

# Mengakses class attribute dari objek
print(p1.TITLES)  

# Mengakses class attribute dari kelas
print(Passenger.TITLES)  

# Mengakses instance attribute dari objek
print(p1.title)  

# Mengakses instance attribute dari kelas
print(Passenger.title)  
