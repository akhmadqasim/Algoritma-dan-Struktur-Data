import time  # Mengimport modul time


def sumOfN2(n):  # Membuat fungsi sumOfN2 dengan parameter n
    start = time.time()  # Membuat variabel start dengan nilai waktu saat ini

    theSum = 0  # Membuat variabel theSum dengan nilai 0
    for i in range(1, n + 1):  # Membuat perulangan dengan nilai awal 1 dan nilai akhir n + 1
        theSum = theSum + i  # Menghitung nilai theSum dengan menjumlahkan nilai theSum dengan nilai i

    end = time.time()  # Membuat variabel end dengan nilai waktu saat ini

    return theSum, end - start  # Mengembalikan nilai theSum dan nilai end - start


for i in range(5):  # Membuat perulangan dengan nilai awal 0 dan nilai akhir 5
    # Menampilkan hasil dari fungsi sumOfN2 dengan parameter 1000
    print("Hasil disoal 4.2a adalah %d membutuhkan waktu %10.7f detik" % sumOfN2(10000))

for i in range(5):  # Membuat perulangan dengan nilai awal 0 dan nilai akhir 5
    # Menampilkan hasil dari fungsi sumOfN2 dengan parameter 100000
    print("Hasil disoal 4.2b adalah %d membutuhkan waktu %10.7f detik" % sumOfN2(100000))

for i in range(5):  # Membuat perulangan dengan nilai awal 0 dan nilai akhir 5
    # Menampilkan hasil dari fungsi sumOfN2 dengan parameter 1000000
    print("Hasil disoal 4.2c adalah %d membutuhkan waktu %10.7f detik" % sumOfN2(1000000))
