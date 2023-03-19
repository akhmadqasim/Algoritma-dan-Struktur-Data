# from pythonds.basic.stack import Stack

class Stack:  # Membuat kelas Stack
    def __init__(self):  # Membuat konstruktor untuk kelas Stack
        self.items = []  # Membuat list kosong

    def isEmpty(self):  # Membuat method untuk mengecek apakah stack kosong
        return self.items == []  # Mengembalikan nilai True jika stack kosong

    def push(self, item):  # Membuat method untuk menambahkan item ke stack
        self.items.append(item)  # Menambahkan item ke stack

    def pop(self):  # Membuat method untuk menghapus item dari stack
        return self.items.pop()  # Menghapus item dari stack dan mengembalikan nilai item

    def peek(self):  # Membuat method untuk melihat item teratas dari stack
        return self.items[len(self.items) - 1]  # Mengembalikan nilai item teratas dari stack

    def size(self):  # Membuat method untuk mengetahui ukuran stack
        return len(self.items)  # Mengembalikan nilai panjang stack


s = Stack()  # Membuat objek s dari kelas Stack

print(s.isEmpty())  # Menampilkan hasil dari method isEmpty
s.push(4)  # Menambahkan item ke stack
s.push('dog')  # Menambahkan item ke stack
print(s.peek())  # Menampilkan hasil dari method peek
s.push(True)  # Menambahkan item ke stack
print(s.size())  # Menampilkan hasil dari method size
print(s.isEmpty())  # Menampilkan hasil dari method isEmpty
s.push(8.4)  # Menambahkan item ke stack
print(s.pop())  # Menampilkan hasil dari method pop
print(s.pop())  # Menampilkan hasil dari method pop
print(s.size())  # Menampilkan hasil dari method size
