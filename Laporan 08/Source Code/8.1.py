def listsum_A(numList):  # fungsi listsum_A dengan parameter numList
    theSum = 0  # inisialisasi variabel theSum dengan nilai 0
    for i in numList:  # perulangan for dengan variabel i di dalam numList
        theSum = theSum + i  # variabel theSum diisi dengan nilai theSum ditambah i
    return theSum  # mengembalikan nilai theSum


print(listsum_A([1, 3, 5, 7, 9]))  # memanggil fungsi listsum_A dengan parameter [1, 3, 5, 7, 9]


def listsum_B(numList):  # fungsi listsum_B dengan parameter numList
    if len(numList) == 1:  # jika panjang numList sama dengan 1
        return numList[0]  # mengembalikan nilai numList ke indeks 0
    else:  # jika tidak
        # mengembalikan nilai numList ke indeks 0 ditambah fungsi listsum_B
        # dengan parameter numList ke indeks 1 sampai akhir
        return numList[0] + listsum_B(numList[1:])


print(listsum_B([1, 3, 5, 7, 9]))  # memanggil fungsi listsum_B dengan parameter [1, 3, 5, 7, 9]

# Analisa dari kedua program di atas adalah:
# Program 8.1a menggunakan perulangan for untuk menjumlahkan semua elemen dalam list.
# Program 8.1b menggunakan rekursi untuk menjumlahkan semua elemen dalam list.
