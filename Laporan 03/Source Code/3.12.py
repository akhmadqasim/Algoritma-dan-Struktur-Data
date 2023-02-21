class Fraksi:  # Definisi kelas Fraksi
    def __init__(self, top, bottom):  # Membuat fungsi __init__ dengan parameter top dan bottom
        self.num = top  # Membuat atribut num dengan nilai top
        self.den = bottom  # Membuat atribut den dengan nilai bottom

    def __add__(self, otherfraction):  # Membuat fungsi __add__ dengan parameter otherFraction
        # Membuat objek baru dengan nilai top dan bottom yang baru
        newnum = self.num * otherfraction.den + self.den * otherfraction.num
        newden = self.den * otherfraction.den  # Membuat atribut newnum dan newden

        return Fraksi(newnum, newden)  # Mengembalikan objek baru


myFraksi = Fraksi(3, 5)  # Membuat objek myFraksi dengan nilai top = 3 dan bottom = 5
print(myFraksi)  # Menampilkan objek myFraksi

f1 = Fraksi(1, 4)  # Membuat objek f1 dengan nilai top = 1 dan bottom = 4
f2 = Fraksi(1, 2)  # Membuat objek f2 dengan nilai top = 1 dan bottom = 2
print(f1 + f2)  # Terjadi error karena tidak ada fungsi __add__ yang didefinisikan
