from pythonds.basic.stack import Stack  # Mengimpor modul Stack


def divideBy2(decNumber):  # Fungsi divideBy2 untuk mengubah bilangan desimal menjadi biner
    remstack = Stack()  # Membuat objek Stack

    while decNumber > 0:  # Melakukan perulangan while
        rem = decNumber % 2  # Membuat variabel rem dengan nilai sisa pembagian decNumber dengan 2
        remstack.push(rem)  # Memasukkan nilai rem ke dalam stack
        decNumber = decNumber // 2  # Membuat variabel decNumber dengan nilai pembagian decNumber dengan 2

    binString = ""  # Membuat variabel binString dengan nilai string kosong
    while not remstack.isEmpty():  # Melakukan perulangan while
        binString = binString + str(remstack.pop())  # Menambahkan nilai binString dengan nilai yang di pop dari stack

    return binString  # Mengembalikan nilai binString


print(divideBy2(42))  # Menampilkan hasil dari fungsi divideBy2
print(divideBy2(55))  # Menampilkan hasil dari fungsi divideBy2
