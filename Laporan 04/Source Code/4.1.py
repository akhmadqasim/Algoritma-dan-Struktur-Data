def foo(joko):  # Membuat fungsi foo dengan parameter joko
    agus = 0  # Membuat variabel agus dengan nilai 0
    for dini in range(1, joko + 1):  # Membuat perulangan dengan nilai awal 1 dan nilai akhir joko + 1
        ayu = dini  # Membuat variabel ayu dengan nilai dini
        agus = agus + ayu  # Menghitung nilai agus dengan menjumlahkan nilai agus dengan nilai ayu

    return agus  # Mengembalikan nilai agus


print(foo(10))  # Menampilkan hasil dari fungsi foo dengan parameter 10


def sumOfN(n):  # Membuat fungsi sumOfN dengan parameter n
    theSum = 0  # Membuat variabel theSum dengan nilai 0
    for i in range(1, n + 1):  # Membuat perulangan dengan nilai awal 1 dan nilai akhir n + 1
        theSum = theSum + i  # Menghitung nilai theSum dengan menjumlahkan nilai theSum dengan nilai i

    return theSum  # Mengembalikan nilai theSum


print(sumOfN(10))  # Menampilkan hasil dari fungsi sumOfN dengan parameter 10
