from pythonds.basic.stack import Stack  # Mengimpor kelas Stack dari modul pythonds.basic.stack

# parChecker merupakan fungsi yang menerima parameter symbolString
# Fungsi ini akan mengembalikan nilai True jika symbolString memiliki jumlah kurung yang sama
def parChecker(symbolString):  # Membuat fungsi parChecker
    s = Stack()  # Membuat objek s dari kelas Stack
    balanced = True  # Membuat variabel balanced dengan nilai True
    index = 0  # Membuat variabel index dengan nilai 0
    # Melakukan perulangan selama index kurang dari panjang symbolString dan balanced bernilai True
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]  # Mengambil nilai symbol dari symbolString
        if symbol == "(":  # Jika symbol bernilai (
            s.push(symbol)  # Menambahkan symbol ke stack
        else:  # Jika symbol tidak bernilai (
            if s.isEmpty():  # Jika stack kosong
                balanced = False  # Mengubah nilai balanced menjadi False karena jumlah kurung tidak sama
            else:  # Jika stack tidak kosong
                s.pop()  # Menghapus item dari stack

        index = index + 1  # Menambahkan nilai index dengan 1

    if balanced and s.isEmpty():  # Jika balanced bernilai True dan stack kosong
        return True  # Mengembalikan nilai True
    else:  # Jika balanced bernilai False atau stack tidak kosong
        return False  # Mengembalikan nilai False


print(parChecker('{{}'))
print(parChecker('{{}}'))


