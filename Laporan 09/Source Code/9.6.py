class HashTable:  # Fungsi HashTable untuk membuat tabel hash
    def __init__(self):  # Fungsi __init__ untuk menginisialisasi tabel hash
        self.size = 11  # ukuran tabel hash
        self.slots = [None] * self.size  # slot untuk menampung nilai
        self.data = [None] * self.size  # data untuk menampung nilai

    def put(self, key, data):  # Fungsi put untuk menambahkan nilai ke dalam tabel hash
        hashvalue = self.hashfunction(key, len(self.slots))  # mengubah nilai menjadi nilai integer

        if self.slots[hashvalue] == None:  # jika slot kosong
            self.slots[hashvalue] = key  # maka nilai akan dimasukkan ke dalam slot
            self.data[hashvalue] = data  # dan nilai akan dimasukkan ke dalam data
        else:  # jika tidak
            if self.slots[hashvalue] == key:  # jika nilai yang dimasukkan sama dengan nilai yang ada di dalam slot
                self.data[hashvalue] = data  # replace
            else:  # jika tidak
                nextslot = self.rehash(hashvalue, len(self.slots))  # maka nilai akan dimasukkan ke dalam slot berikut
                # selama slot tidak kosong dan nilai yang dimasukkan tidak sama dengan nilai yang ada di dalam slot
                while self.slots[nextslot] != None and \
                        self.slots[nextslot] != key:  # maka nilai akan dimasukkan ke dalam slot berikut
                    # selama slot tidak kosong dan nilai yang dimasukkan tidak sama dengan nilai yang ada di dalam slot
                    nextslot = self.rehash(nextslot, len(self.slots))

                if self.slots[nextslot] == None:  # jika slot kosong
                    self.slots[nextslot] = key  # maka nilai akan dimasukkan ke dalam slot
                    self.data[nextslot] = data  # dan nilai akan dimasukkan ke dalam data
                else:  # jika tidak
                    self.data[nextslot] = data  # replace

    def hashfunction(self, key, size):  # Fungsi hashfunction untuk mengubah nilai menjadi nilai integer
        return key % size  # mengembalikan nilai

    def rehash(self, oldhash, size):  # Fungsi rehash untuk mengubah nilai menjadi nilai integer
        return (oldhash + 1) % size  # mengembalikan nilai

    def get(self, key):  # Fungsi get untuk mengambil nilai dari tabel hash
        startslot = self.hashfunction(key, len(self.slots))  # mengubah nilai menjadi nilai integer

        data = None  # nilai awal
        stop = False  # nilai awal
        found = False  # nilai awal
        position = startslot  # posisi awal
        # selama slot tidak kosong dan nilai yang dimasukkan tidak sama dengan nilai yang ada di dalam slot
        while self.slots[position] != None and \
                not found and not stop:  # maka nilai akan dimasukkan ke dalam slot berikut
            if self.slots[position] == key:  # jika nilai yang dimasukkan sama dengan nilai yang ada di dalam slot
                found = True  # maka nilai akan dimasukkan ke dalam slot
                data = self.data[position]  # dan nilai akan dimasukkan ke dalam data
            else:  # jika tidak
                position = self.rehash(position, len(self.slots))  # maka nilai akan dimasukkan ke dalam slot berikut
                if position == startslot:  # jika posisi sama dengan posisi awal
                    stop = True  # maka nilai akan dimasukkan ke dalam slot
        return data  # mengembalikan nilai

    def __getitem__(self, key):  # Fungsi __getitem__ untuk mengambil nilai dari tabel hash
        return self.get(key)  # mengembalikan nilai

    def __setitem__(self, key, data):  # Fungsi __setitem__ untuk menambahkan nilai ke dalam tabel hash
        self.put(key, data)  # menambahkan nilai ke dalam tabel hash


H = HashTable()  # membuat tabel hash
H[54] = "cat"  # menambahkan nilai ke dalam tabel hash
H[26] = "dog"  # menambahkan nilai ke dalam tabel hash
H[93] = "lion"  # menambahkan nilai ke dalam tabel hash
H[17] = "tiger"  # menambahkan nilai ke dalam tabel hash
H[77] = "bird"  # menambahkan nilai ke dalam tabel hash
H[31] = "cow"  # menambahkan nilai ke dalam tabel hash
H[44] = "goat"  # menambahkan nilai ke dalam tabel hash
H[55] = "pig"  # menambahkan nilai ke dalam tabel hash
H[20] = "chicken"  # menambahkan nilai ke dalam tabel hash
print(H.slots)  # menampilkan slot
print(H.data)  # menampilkan data

print(H[20])  # mengambil nilai dari tabel hash

print(H[17])  # mengambil nilai dari tabel hash
H[20] = 'duck'  # menambahkan nilai ke dalam tabel hash
print(H[20])  # mengambil nilai dari tabel hash
print(H[99])  # mengambil nilai dari tabel hash
