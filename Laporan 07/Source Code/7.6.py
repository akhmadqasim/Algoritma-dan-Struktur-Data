class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext


class UnorderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())


mylist = UnorderedList()  # Membuat objek mylist dengan nilai UnorderedList()

mylist.add(31)  # Menambahkan nilai 31 ke dalam mylist
mylist.add(77)  # Menambahkan nilai 77 ke dalam mylist
mylist.add(17)  # Menambahkan nilai 17 ke dalam mylist
mylist.add(93)  # Menambahkan nilai 93 ke dalam mylist
mylist.add(26)  # Menambahkan nilai 26 ke dalam mylist
mylist.add(54)  # Menambahkan nilai 54 ke dalam mylist

print(mylist.size())  # Menampilkan panjang dari mylist
print(mylist.search(93))  # Menampilkan apakah 93 ada di dalam mylist
print(mylist.search(100))  # Menampilkan apakah 100 ada di dalam mylist

mylist.add(100)  # Menambahkan nilai 100 ke dalam mylist
print(mylist.search(100))  # Menampilkan apakah 100 ada di dalam mylist
print(mylist.size())  # Menampilkan panjang dari mylist

mylist.remove(54)  # Menghapus nilai 54 dari mylist
print(mylist.size())  # Menampilkan panjang dari mylist
mylist.remove(93)  # Menghapus nilai 93 dari mylist
print(mylist.size())  # Menampilkan panjang dari mylist
mylist.remove(31)  # Menghapus nilai 31 dari mylist
print(mylist.size())  # Menampilkan panjang dari mylist
print(mylist.search(93))  # Menampilkan apakah 93 ada di dalam mylist
