class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


q = Queue()  # Membuat objek Queue

q.enqueue(4)  # Memasukkan nilai 4 ke dalam queue
q.enqueue('dog')  # Memasukkan nilai 'dog' ke dalam queue
q.enqueue(True)  # Memasukkan nilai True ke dalam queue

print(q.size())  # Menampilkan berapa banyak item dari queue
print(q.isEmpty())  # Menampilkan apakah queue kosong atau tidak
print(q.enqueue(8.4))  # Memasukkan nilai 8.4 ke dalam queue
print(q.dequeue())  # Menghapus nilai dari queue dan menampilkan nilai yang dihapus
print(q.dequeue())  # Menghapus nilai dari queue dan menampilkan nilai yang dihapus
print(q.size())  # Menampilkan berapa banyak item dari queue
