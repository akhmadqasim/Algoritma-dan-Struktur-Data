from pythonds.basic.stack import Stack  # Mengimpor modul Stack


def baseConverter(decNumber, base):  # Fungsi baseConverter untuk mengubah bilangan desimal menjadi bilangan lain
    # Variabel digits untuk menyimpan nilai dari 0-9 dan A-F
    # yang akan digunakan untuk mengubah bilangan desimal menjadi bilangan lain
    digits = "0123456789ABCDEF"

    remstack = Stack()  # Membuat objek Stack

    while decNumber > 0:  # Melakukan perulangan while
        rem = decNumber % base  # Membuat variabel rem dengan nilai sisa pembagian decNumber dengan base
        remstack.push(rem)  # Memasukkan nilai rem ke dalam stack
        decNumber = decNumber // base  # Membuat variabel decNumber dengan nilai pembagian decNumber dengan base

    newString = ""  # Membuat variabel newString dengan nilai string kosong
    while not remstack.isEmpty():  # Melakukan perulangan while
        # Menambahkan nilai newString dengan nilai yang di pop dari stack
        newString = newString + digits[remstack.pop()]

    return newString  # Mengembalikan nilai newString


print(baseConverter(25, 2))  # Merubah bilangan desimal menjadi bilangan biner
print(baseConverter(25, 16))  # Merubah bilangan desimal menjadi bilangan heksadesimal
