# Fungsi Hash mengubah string menjadi nilai integer yang akan digunakan untuk menentukan
# posisi dari string tersebut di dalam tabel hash.

def hash(astring, tablesize):  # Fungsi hash berfungsi untuk mengubah string menjadi nilai integer
    sum = 0  # nilai awal
    for pos in range(len(astring)):  # selama posisi masih kurang dari panjang string
        sum = sum + ord(astring[pos])  # nilai akan ditambah dengan nilai ordinal dari karakter yang ada di string
    return sum % tablesize  # mengembalikan nilai


myString = "cari"  # string yang akan diubah menjadi nilai integer
print(hash(myString, 11))  # mengubah string menjadi nilai integer

myString = "?"  # string yang akan diubah menjadi nilai integer
print(hash(myString, 11))  # mengubah string menjadi nilai integer
