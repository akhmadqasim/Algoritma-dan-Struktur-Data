MyList = [1, 3, True, 6.5]  # List berisi integer, boolean, dan float
print(MyList)  # Menampilkan isi variabel MyList
A = [MyList] * 3  # Membuat list A yang berisi 3 kalinya list MyList
print(A)  # Menampilkan isi variabel A
MyList[2] = 45  # Mengubah isi list MyList pada indeks ke-2 menjadi 45
print(A)  # Menampilkan isi variabel A

myList_A = [1024, 3, True, 6.5]  # List berisi integer, boolean, dan float
myList_A.append(False)  # Menambahkan elemen False ke list myList_A
print(myList_A)  # Menampilkan isi variabel myList_A
myList_A.insert(2, 4.5)  # Menambahkan elemen 4.5 ke list myList_A pada indeks ke-2
print(myList_A)  # Menampilkan isi variabel myList_A
print(myList_A.pop())  # Menghapus elemen terakhir dari list myList_A
print(myList_A)  # Menampilkan isi variabel myList_A
print(myList_A.pop(1))  # Menghapus elemen pada indeks ke-1 dari list myList_A
print(myList_A)  # Menampilkan isi variabel myList_A
myList_A.pop(2)  # Menghapus elemen pada indeks ke-2 dari list myList_A
print(myList_A)  # Menampilkan isi variabel myList_A
myList_A.sort()  # Mengurutkan elemen list myList_A
print(myList_A)  # Menampilkan isi variabel myList_A yang diurutkan
myList_A.reverse()  # Membalik urutan elemen list myList_A
print(myList_A)  # Menampilkan isi variabel myList_A yang telah dibalik
print(myList_A.count(6.5))  # Menghitung jumlah kemunculan elemen 6.5 pada list myList_A
print(myList_A.index(4.5))  # Menampilkan indeks elemen 4.5 pada list myList_A
myList_A.remove(6.5)  # Menghapus elemen 6.5 pada list myList_A
print(myList_A)  # Menampilkan isi variabel myList_A
del myList_A[0]  # Menghapus elemen pada indeks ke-0 dari list myList_A
print(myList_A)  # Menampilkan isi variabel myList_A

# Contoh "+" dalam penggunaan list
myList_A = [1, 2, 3]
myList_B = [4, 5, 6]
print(myList_A + myList_B)

# Contoh "len" dalam penggunaan list
myList_A = [1, 2, 3]
print(len(myList_A))

# Contoh [:] dalam penggunaan list
myList_A = [1, 2, 3]
print(myList_A[1:])
