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


class OrderedList:
    def __init__(self):
        self.head = None

    def search(self, item):
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.getData() == item:
                found = True
            else:
                if current.getData() > item:
                    stop = True
                else:
                    current = current.getNext()

        return found

    def add(self, item):
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()

        temp = Node(item)
        if previous == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)

    def isEmpty(self):
        return self.head == None

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count


mylist = OrderedList()  # Membuat objek mylist dengan nilai OrderedList()
mylist.add(31)  # Menambahkan nilai 31 ke dalam mylist
mylist.add(77)  # Menambahkan nilai 77 ke dalam mylist
mylist.add(17)  # Menambahkan nilai 17 ke dalam mylist
mylist.add(93)  # Menambahkan nilai 93 ke dalam mylist
mylist.add(26)  # Menambahkan nilai 26 ke dalam mylist
mylist.add(54)  # Menambahkan nilai 54 ke dalam mylist

print(mylist.size())  # Menampilkan panjang dari mylist
print(mylist.search(93))  # Menampilkan apakah nilai 93 ada di dalam mylist
print(mylist.search(100))  # Menampilkan apakah nilai 100 ada di dalam mylist
