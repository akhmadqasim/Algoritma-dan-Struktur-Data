# Dilakukan perulangan untuk setiap huruf pada string
# Jika huruf tersebut bukan huruf vokal, maka akan ditambahkan ke dalam list
# Huruf akan diubah menjadi huruf kapital
namaTanpaKonsonan = [ch.upper() for ch in "Akhmad Qasim" if ch not in " aeiou"]
print(namaTanpaKonsonan)  # Menampilkan list namaTanpaKonsonan
