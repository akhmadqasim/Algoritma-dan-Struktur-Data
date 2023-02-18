# Menampilkan hasil dari beberapa contoh method
print("Berikut ini adalah hasil contoh fragment dari (54).__ad__(21) : \n", (54).__add__(21))

print(range(10))  # Menampilkan range(0, 10)
print(list(range(10)))  # Menampilkan list dari range 0 sampai 9
print(list(range(5, 10)))  # Menampilkan list dari range 5 sampai 9
print(list(range(5, 15, 3)))  # Menampilkan list dari range 5 sampai 14 dengan interval 3
print(list(range(10, 1, -1)))  # Menampilkan list dari range 10 sampai 2 dengan interval -1

myName = "Akhmad Qasim"  # String berisi nama "Akhmad Qasim"
print(len(myName))  # Menampilkan panjang string myName
print(myName[3])  # Menampilkan karakter ke-4 dari string myName
print(list(myName))  # Menampilkan list dari string myName
print(myName.upper())  # Menampilkan string myName dalam huruf kapital
print(myName.center(10))  # Menampilkan string myName menjadi yang di tengah dengan lebar 10
print(myName.find("a"))  # Menampilkan indeks dari karakter "a" pada string myName
print(myName.split("a"))  # Menampilkan list dari string myName yang dipisahkan oleh karakter "a"

# Contoh count() pada myName
print(myName.count("a"))  # Menampilkan jumlah kemunculan karakter "a" pada string myName

# Contoh ljus() pada myName
print(myName.ljust(20))  # Menampilkan string myName menjadi yang di kiri dengan lebar 20

# Contoh rjust() pada myName
print(myName.rjust(20))  # Menampilkan string myName menjadi yang di kanan dengan lebar 20
