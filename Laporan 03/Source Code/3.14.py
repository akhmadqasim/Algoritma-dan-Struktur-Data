class Fraksi:  # Definisi kelas Fraksi
    def __init__(self, top, bottom):  # Membuat fungsi __init__ dengan parameter top dan bottom
        self.num = top  # Membuat atribut num dengan nilai top
        self.den = bottom  # Membuat atribut den dengan nilai bottom

    def __eq__(self, other):  # Membuat fungsi __eq__ dengan parameter other
        firstnum = self.num * other.den  # Membuat atribut firstnum
        secondnum = other.num * self.den  # Membuat atribut secondnum

        return firstnum == secondnum  # Mengembalikan nilai firstnum == secondnum


myFraksi = Fraksi(3, 5)  # Membuat objek myFraksi dengan nilai top = 3 dan bottom = 5
print(myFraksi)  # Menampilkan objek myFraksi

x = Fraksi(1, 2)  # Membuat objek x dengan nilai top = 1 dan bottom = 2
y = Fraksi(2, 3)  # Membuat objek y dengan nilai top = 2 dan bottom = 3
print(x + y)  # Terdapat error karena
print(x == y)  # Menampilkan objek x == y
