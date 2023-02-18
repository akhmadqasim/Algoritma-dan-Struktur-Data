price = 5800  # Variable price bertipe integer dengan nilai 5800
item = "pisang"  # Variable item bertipe string dengan nilai "pisang"
print("Harga sebuah %s adalah %d rupiah" % (item, price))  # Menampilkan hasil dengan format string
print("Harga sebuah %+10s adalah %5.2f rupiah" % (item, price))  # Menampilkan hasil dengan format string dan padding
print("Harga sebuah %+10s adalah %10.2f rupiah" % (item, price))  # Menampilkan hasil dengan format string dan padding
itemdict = {"item": "pisang", "harga": 6800}  # Variable itemdict bertipe dictionary
print("Harga sebuah %(item)s adalah %(harga)7.1f rupiah" % itemdict)  # Menampilkan hasil format string dan padding

# %+10s adalah padding untuk menambahkan spasi sebanyak 10 karakter
# %5.2f adalah format float dengan 5 karakter total dan 2 karakter dibelakang koma