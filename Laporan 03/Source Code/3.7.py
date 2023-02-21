import math

anumber = int(input("Masukan nilai integer"))
# cara mengatasi hal tersebut adalah dengan menambahkan fungsi try dan except
try:
    print(math.sqrt(anumber))
except:
    print("Mohan Maaf, nilai yang anda input adalah bilangan negatif")
