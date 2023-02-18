aName = input("Nama: ")  # Input nama
myNim = int(input("Nim: "))  # Input nim

print(aName, myNim)  # Menampilkan nama dan nim
print(aName, myNim, sep="-", end=".")
print("%s mempunyai NIM %i" % (aName, myNim))
