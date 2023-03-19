from pythonds.basic.stack import Stack  # Mengimpor modul Stack


def parChecker(symbolString):  # Membuat fungsi parChecker
    s = Stack()  # Membuat objek Stack
    balanced = True  # Membuat variabel balanced dengan nilai True
    index = 0  # Membuat variabel index dengan nilai 0
    while index < len(symbolString) and balanced:  # Melakukan perulangan while
        symbol = symbolString[index]  # Membuat variabel symbol dengan nilai symbolString[index]
        if symbol in "([{":  # Jika salah satu symbol berada di dalam "([{"
            s.push(symbol)  # Maka masukkan nilai symbol ke dalam stack
        else:  # Maka jika tidak
            if s.isEmpty():  # Jika stack kosong
                balanced = False  # Maka variabel balanced akan bernilai False
            else:  # Maka jika tidak
                top = s.pop()  # Maka variabel top akan bernilai nilai yang di pop dari stack
                if not matches(top, symbol):  # Jika nilai top dan symbol tidak sama
                    balanced = False  # Maka variabel balanced akan bernilai False

        index = index + 1  # Menambahkan nilai index dengan 1

    if balanced and s.isEmpty():  # Jika variabel balanced bernilai True dan stack kosong
        return True  # Maka kembalikan nilai True
    else:  # Maka jika tidak
        return False  # Maka kembalikan nilai False


def matches(open, close):  # Membuat fungsi matches berfungsi untuk mengecek apakah open dan close sama
    opens = "([{"  # Membuat variabel opens dengan nilai "([{"
    closers = ")]}"  # Membuat variabel closers dengan nilai ")]}"
    return opens.index(open) == closers.index(close)  # Mengembalikan nilai True jika open dan close sama


print(parChecker('{{([][])}()}'))  # Menampilkan hasil dari fungsi parChecker
print(parChecker('[{()]'))  # Menampilkan hasil dari fungsi parChecker
