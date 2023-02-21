class Fraksi:  # Definisi kelas Fraksi
    def __init__(self, top, bottom):  # Membuat fungsi __init__ dengan parameter top dan bottom
        self.num = top  # Membuat atribut num dengan nilai top
        self.den = bottom  # Membuat atribut den dengan nilai bottom

    def __str__(self):  # Berfungsi untuk mengambil nilai dari objek
        return str(self.num) + "/" + str(self.den)  # Mengembalikan nilai berupa string

    def show(self):  # Berfungsi untuk menampilkan nilai dari objek
        print("myFraksi = ", self.num, "/", self.den)


myFraksi = Fraksi(3, 5)  # Membuat objek myFraksi dengan nilai top = 3 dan bottom = 5
print(myFraksi)  # Menampilkan objek myFraksi
myFraksi.show()  # Menampilkan objek myFraksi dengan fungsi show()
