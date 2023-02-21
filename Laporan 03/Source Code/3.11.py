class Fraksi:  # Definisi kelas Fraksi
    def __init__(self, top, bottom):  # Membuat fungsi __init__ dengan parameter top dan bottom
        self.num = top  # Membuat atribut num dengan nilai top
        self.den = bottom  # Membuat atribut den dengan nilai bottom

    # Fungsi __str__ akan dipanggil ketika objek di print
    def __str__(self):  # Berfungsi untuk mengambil nilai dari objek dan
        return str(self.num) + "/" + str(self.den)  # Mengembalikan nilai berupa string

myFraksi = Fraksi(3, 5)  # Membuat objek myFraksi dengan nilai top = 3 dan bottom = 5
print(myFraksi)  # Menampilkan objek myFraksi

myf = Fraksi(3, 5)  # Membuat objek myf dengan nilai top = 3 dan bottom = 5
print(myf)  # Menampilkan objek myf
print("Saya makan", myf, "dari kue hamparan tatak")  # Menampilkan objek myf
