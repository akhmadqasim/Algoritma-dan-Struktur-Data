class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0, item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)


d = Deque()  # Membuat objek d dengan nilai Deque()
print(d.isEmpty())  # Menampilkan apakah d kosong
d.addRear(4)  # Menambahkan nilai 4 ke dalam d
d.addRear('dog')  # Menambahkan nilai 'dog' ke dalam d
d.addFront('cat')  # Menambahkan nilai 'cat' ke dalam d
d.addFront(True)  # Menambahkan nilai True ke dalam d
print(d.size())  # Menampilkan panjang dari d
print(d.isEmpty())  # Menampilkan apakah d kosong
d.addRear(8.4)  # Menambahkan nilai 8.4 ke dalam d
print(d.removeRear())  # Menampilkan nilai yang dihapus dari d
print(d.removeFront())  # Menampilkan nilai yang dihapus dari d
