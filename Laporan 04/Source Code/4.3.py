import time  # Mengimport modul time

def sumOfN3(n):  # Membuat fungsi sumOfN3 dengan parameter n
    start = time.time()  # Membuat variabel start dengan nilai waktu saat ini
    result = (n * (n + 1)) / 2  # Mengembalikan nilai n * (n + 1) / 2
    time.sleep(0.00000001)  # Menunda eksekusi selama 0.00000001 detik
    end = time.time()  # Membuat variabel end dengan nilai waktu saat ini
    return result, end - start  # Mengembalikan nilai theSum dan nilai end - start


# Menampilkan hasil dari fungsi sumOfN3 dengan parameter 10000
print("Hasil 10000 iterasi adalah %d memerlukan %10.7f detik" % sumOfN3(10000))
# Menampilkan hasil dari fungsi sumOfN3 dengan parameter 100000
print("Hasil 100000 iterasi adalah %d memerlukan %10.7f detik" % sumOfN3(100000))
# Menampilkan hasil dari fungsi sumOfN3 dengan parameter 1000000
print("Hasil 1000000 iterasi adalah %d memerlukan %10.7f detik" % sumOfN3(1000000))

# Jelas bahwa fungsi sumOfN3 lebih cepat daripada fungsi sumOfN2
# Hal ini dikarenakan fungsi sumOfN3 hanya melakukan 1 perhitungan
# Sedangkan fungsi sumOfN2 melakukan perhitungan sebanyak n + 1 menggunakan perulangan