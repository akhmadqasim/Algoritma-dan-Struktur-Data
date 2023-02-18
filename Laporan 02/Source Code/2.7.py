mySet = {3, 6, "kucing", 4.5, False}  # Set berisi integer, string, dan boolean
print(mySet)  # Menampilkan isi variabel mySet
print(len(mySet))  # Menampilkan panjang set mySet
print(False in mySet)  # Menampilkan apakah elemen False ada di dalam set mySet
print("cat" in mySet)  # Menampilkan apakah elemen "cat" ada di dalam set mySet

yourSet = {99, 3, 100, "kuda"}  # Set berisi integer, string, dan boolean
print(mySet.union(yourSet))  # Menampilkan gabungan dari set mySet dan yourSet
print(mySet | yourSet)  # Menampilkan gabungan dari set mySet dan yourSet
print(mySet.intersection(yourSet))  # Menampilkan irisan dari set mySet dan yourSet
print(mySet & yourSet)  # Menampilkan irisan dari set mySet dan yourSet
print(mySet.difference(yourSet))  # Menampilkan selisih dari set mySet dan yourSet
print(mySet - yourSet)  # Menampilkan selisih dari set mySet dan yourSet
print({3100}.issubset(yourSet))  # Menampilkan apakah set {3100} merupakan subset dari yourSet
print({3100} <= yourSet)  # Menampilkan apakah set {3100} merupakan subset dari yourSet

mySet.add("rumah")  # Menambahkan elemen "rumah" ke dalam set mySet
print(mySet)  # Menampilkan isi variabel mySet
mySet.remove(4.5)  # Menghapus elemen 4.5 dari set mySet
print(mySet)  # Menampilkan isi variabel mySet
print(mySet.pop())  # Menghapus elemen acak dari set mySet
print(mySet)  # Menampilkan isi variabel mySet

mySet.clear()  # Menghapus semua elemen dari set mySet
print(mySet)  # Menampilkan isi variabel mySet
