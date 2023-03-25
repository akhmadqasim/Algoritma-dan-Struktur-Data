from pythonds.basic.deque import Deque  # Mengimpor modul Deque


def palchecker(aString):  # Membuat fungsi palchecker
    chardeque = Deque()  # Membuat objek chardeque dengan nilai Deque()

    for ch in aString:  # Melakukan perulangan untuk setiap nilai ch dalam aString
        chardeque.addRear(ch)  # Menambahkan nilai ch ke dalam chardeque

    stillEqual = True  # Membuat variabel stillEqual dengan nilai True

    # Melakukan perulangan selama chardeque lebih besar dari 1 dan stillEqual bernilai True
    while chardeque.size() > 1 and stillEqual:
        # Menghapus nilai pertama dari chardeque dan menyimpannya ke dalam variabel first
        first = chardeque.removeFront()
        # Menghapus nilai terakhir dari chardeque dan menyimpannya ke dalam variabel last
        last = chardeque.removeRear()
        if first != last:  # Jika first tidak sama dengan last
            stillEqual = False  # Maka nilai stillEqual akan bernilai False

    return stillEqual  # Mengembalikan nilai stillEqual


print(palchecker("lsdkjfskf"))  # Mencetak hasil dari palchecker("lsdkjfskf")
print(palchecker("radar"))  # Mencetak hasil dari palchecker("radar")
