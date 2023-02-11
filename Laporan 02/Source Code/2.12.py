price = 5800
item = "pisang"
print("Harga sebuah %s adalah %d rupiah" % (item, price))
print("Harga sebuah %+10s adalah %5.2f rupiah" % (item, price))
print("Harga sebuah %+10s adalah %10.2f rupiah" % (item, price))
itemdict = {"item": "pisang", "harga": 6800}
print("Harga sebuah %(item)s adalah %(cost)7.1f rupiah" % itemdict)
