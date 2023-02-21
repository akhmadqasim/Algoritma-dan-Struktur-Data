import math  # Memanggil modul math

n = int(input("Masukkan angka "))  # Meminta input angka
if n < 0:  # Jika angka yang di input negatif
    print("Maaf, nilai yang di input adalah negatif")  # Maka akan menampilkan pesan error
else:  # Jika angka yang di input positif
    print(math.sqrt(n))  # Maka akan menampilkan hasil akar dari angka yang di input
