MyNim = str(2211102441237)  # Merubah tipe data integer ke string

MyNim_10th = MyNim[9]  # Mengambil karakter ke-10 dari string MyNim
MyNim_11th = MyNim[-3]  # Mengambil karakter ke-3 dari belakang (11) string MyNim
i = 11
MyNim_12th = MyNim[i]  # Mengambil karakter ke-12 dari string MyNim
MyNim_13th = MyNim[i+1]  # Mengambil karakter ke-13 dari string MyNim
a = int(MyNim_10th + MyNim_11th)  # Merubah tipe data string ke integer
b = int(MyNim_12th + MyNim_13th)  # Merubah tipe data string ke integer

print(MyNim)  # Menampilkan isi variabel MyNim
print(MyNim_10th)  # Menampilkan isi variabel MyNim_10th
print(MyNim_11th)  # Menampilkan isi variabel MyNim_11th
print(MyNim_12th)  # Menampilkan isi variabel MyNim_12th
print(MyNim_13th)  # Menampilkan isi variabel MyNim_13th
print(a)  # Menampilkan isi variabel a, yaitu 24
print("nilai float b = ", b)  # Menampilkan isi variabel b, yaitu 37
