import time  # Mengimport modul time

# Ini termasuk Notasi Big O dengan Notasi O(n^2)
def sumOfY(n):  # Membuat fungsi sumOfY dengan parameter n
    start = time.time()  # Membuat variabel start dengan nilai waktu saat ini

    theSum = 0  # Membuat variabel theSum dengan nilai 0
    for i in range(n):  # Membuat perulangan dengan nilai awal 0 dan nilai akhir n
        for j in range(n):  # Membuat perulangan dengan nilai awal 0 dan nilai akhir n
            theSum = theSum + i * j  # Menghitung nilai theSum dengan menjumlahkan nilai theSum dengan nilai i * j
    end = time.time()  # Membuat variabel end dengan nilai waktu saat ini
    return theSum, end - start  # Mengembalikan nilai theSum dan nilai end - start


# Menampilkan hasil dari fungsi sumOfY dengan parameter 1000
print("Hasill sumOfY(1000) adalah %d membutuhkan waktu %10.3f detik" % sumOfY(1000))
# Menampilkan hasil dari fungsi sumOfY dengan parameter 2000
print("Hasill sumOfY(2000) adalah %d membutuhkan waktu %10.3f detik" % sumOfY(2000))
# Menampilkan hasil dari fungsi sumOfY dengan parameter 3000
print("Hasill sumOfY(3000) adalah %d membutuhkan waktu %10.3f detik" % sumOfY(3000))
# Menampilkan hasil dari fungsi sumOfY dengan parameter 4000
print("Hasill sumOfY(4000) adalah %d membutuhkan waktu %10.3f detik" % sumOfY(4000))
# Menampilkan hasil dari fungsi sumOfY dengan parameter 5000
print("Hasill sumOfY(5000) adalah %d membutuhkan waktu %10.3f detik" % sumOfY(5000))
# Menampilkan hasil dari fungsi sumOfY dengan parameter 6000
print("Hasill sumOfY(6000) adalah %d membutuhkan waktu %10.3f detik" % sumOfY(6000))
# Menampilkan hasil dari fungsi sumOfY dengan parameter 7000
print("Hasill sumOfY(7000) adalah %d membutuhkan waktu %10.3f detik" % sumOfY(7000))
# Menampilkan hasil dari fungsi sumOfY dengan parameter 8000
print("Hasill sumOfY(8000) adalah %d membutuhkan waktu %10.3f detik" % sumOfY(8000))
# Menampilkan hasil dari fungsi sumOfY dengan parameter 9000
print("Hasill sumOfY(9000) adalah %d membutuhkan waktu %10.3f detik" % sumOfY(9000))
# Menampilkan hasil dari fungsi sumOfY dengan parameter 10000
print("Hasill sumOfY(10000) adalah %d membutuhkan waktu %10.3f detik" % sumOfY(10000))
