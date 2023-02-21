class Fraksi:  # Definisi kelas Fraksi
    def __init__(self, top, bottom):  # Membuat fungsi __init__ dengan parameter top dan bottom
        self.num = top  # Membuat atribut num dengan nilai top
        self.den = bottom  # Membuat atribut den dengan nilai bottom

    def __add__(self, otherfraction):  # Membuat fungsi __add__ dengan parameter otherFraction
        newnum = self.num * otherfraction.den + self.den * otherfraction.num  # Membuat atribut newnum
        newden = self.den * otherfraction.den  # Membuat atribut newden
        common = gcd(newnum, newden)  # Membuat atribut common dengan nilai gcd dari newnum dan newden
        return Fraksi(newnum // common, newden // common)  # Mengembalikan objek baru


def gcd(m, n):  # Membuat fungsi gcd dengan parameter m dan n
    while m % n != 0:  # Membuat perulangan while dengan kondisi m mod n tidak sama dengan 0
        oldm = m  # Membuat atribut oldm dengan nilai m
        oldn = n  # Membuat atribut oldn dengan nilai n

        m = oldn  # Mengubah nilai m dengan nilai oldn
        n = oldm % oldn  # Mengubah nilai n dengan nilai oldm mod oldn

    return n  # Mengembalikan nilai n


myFraksi = Fraksi(3, 5)  # Membuat objek myFraksi dengan nilai top = 3 dan bottom = 5
print(myFraksi)  # Menampilkan objek myFraksi

f1 = Fraksi(1, 4)  # Membuat objek f1 dengan nilai top = 1 dan bottom = 4
f2 = Fraksi(1, 2)  # Membuat objek f2 dengan nilai top = 1 dan bottom = 2
print(f1 + f2)  # Menampilkan objek f1 + f2
